import { saveImageToFile } from "./same-image.ts"
import path from "path"
import { open } from "fs"
import { openai } from "@config/openai.ts"
import { env } from "./env.ts"
import Bluebird from "bluebird"

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

      const filename = `${safePromptBase}_${i + 1}_${seed}.png`
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

export async function generateImage(
  prompt: string,
  N: number,
  seed: number
): Promise<void> {
  if (N > 1) {
    let promises: Array<Promise<void>> = []

    for (let i = 0; i < N; i++) {
      promises.push(generateImage(prompt, 1, seed + i))
    }

    await Bluebird.map(
      promises,
      async (p) => {
        // console.log(p)
        await p
      },
      {
        concurrency: promises.length,
      }
    )

    return
  }

  console.log(`prompt=${prompt}; N=${N}; seed=${seed}`)

  try {
    const response = await openai.images.generate({
      prompt, // The text prompt for image generation
      // model: "playground-v2-1024px-aesthetic",
      model:
        "fireworks::accounts/fireworks/models/playground-v2-5-1024px-aesthetic",
      // model: "fireworks::accounts/yi-01-ai/models/yi-large"

      // model: "fireworks::accounts/fireworks/models/playground-v2-5-1024px-aesthetic"
      // n: N, //Doesn't work
      // size: "1024x1024", // Image resolution (can be 256x256, 512x512, or 1024x1024)
    })

    console.log(response)

    await handleImageResponse(response, prompt, seed)

    // console.log("Generated Image URL:", response.data[0].url);
  } catch (error) {
    console.error("Error generating image:", error)
  }
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

main()
