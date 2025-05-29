import { getImageBase64, saveImageToFile } from "./same-image.ts"
import path from "path"
import { open } from "fs"
import { openai } from "@config/openai.ts"
import { env } from "./env.ts"
import Bluebird from "bluebird"
import { getRandomInt } from "./random.ts"

export const handleImageResponse = async (
  response: any,
  prompt: string,
  seed: number
) => {
  const outputDir = process.env.OUTPUT_DIR ?? ""

  if (
    response.data &&
    Array.isArray(response.data) &&
    response.data.length > 0
  ) {
    const safePromptBase = prompt.replace(/[^a-zA-Z0-9]/g, "-").substring(0, 80) // Keep room for index to avoid long filenames

    const savedPaths: string[] = []

    for (let i = 0; i < response.data.length; i++) {
      const image = response.data[i]

      if (!image?.b64_json) continue

      const filename = `${safePromptBase}_${i + 1}_${seed}.jpg`
      const filePath = path.join(outputDir, filename)

      await saveImageToFile(image.b64_json, filePath)
      console.log(`Image seed=${seed} i=${i + 1} saved to: ${filePath}`)
      savedPaths.push(filePath)
    }

    return savedPaths
  } else {
    throw new Error("No image data found in the API response")
  }
}


interface DTOImageGenerate{
  prompt: string;
  N: number;
  seed: number;
  size?:string; // Image resolution (can be 256x256, 512x512, or 1024x1024)
}

export async function generateImage(dto: DTOImageGenerate): Promise<Boolean> {
  let { prompt, N, seed, size } = dto
  
  if (N > 1) {
    let promises: Array<Promise<Boolean>> = []

    for (let i = 0; i < N; i++) {
      let seedI:number

      // seedI = getRandomInt(-i, seed);

      // seed = i
      seedI = seed + i * N + seed % 1000 // Ensure different seeds for each image

      // seed = i
      promises.push(generateImage({
        prompt,
        N: 1,
        seed: seedI,
        size: size
      }))
    }

    let result = await Bluebird.map(
      promises,
      async (p:Promise<Boolean>) => {
        // console.log(p)
        return await p
      },
      {
        concurrency: promises.length,
      }
    )

    console.log("Generated images:", result)


    const noOfFailures = result.filter(res => res === false).length;

    if (noOfFailures > 0) {
      console.log("Failures>0")
      return generateImage({prompt,N: noOfFailures,seed:seed + N+noOfFailures})
    }


    return true
    // return result.every((r) => r === true)
  }

  console.log(`prompt=${prompt}; N=${N}; seed=${seed}`)

  try {
    const response = await openai.images.generate({
      prompt, 
      model:
        "fireworks::accounts/fireworks/models/playground-v2-5-1024px-aesthetic",
        
        // controlImage: await getImageBase64("./utils/A_futuristic_cityscape_with_flying_cars_and_neon_lights.png"), // Control image path
        // n: N, //Doesn't work
        
        
        // @ts-ignore
        seed, // Random seed for reproducibility
        size ,
      })

    // console.log(response)

    await handleImageResponse(response, prompt, seed)

    // console.log("Generated Image URL:", response.data[0].url);
  } catch (error) {
    console.error(`Error generating image - ${seed}`, error)

    return false
  }

  return true
}

export async function editImage(
  imagePath: string,
  prompt: string
): Promise<void> {
  console.log(`Editing image=${imagePath} with prompt=${prompt}`)

  try {
    const response = await openai.images.edit({
      image: imagePath,
      prompt,
      model:
        "fireworks::accounts/fireworks/models/playground-v2-5-1024px-aesthetic",
    })

    await handleImageResponse(response, prompt, 0)
  } catch (error) {
    console.error("Error editing image:", error)
  }
}

// Example usage

async function main() {
  const prompt = "A futuristic cityscape with flying cars and neon lights"

  console.log("Prompt : " + prompt)
  // await generateImage(prompt,1);

  await editImage(
    path.join("A_futuristic_cityscape_with_flying_cars_and_neon_lights.png"),
    "Cars should be rolls royce"
  )
}

// main()
