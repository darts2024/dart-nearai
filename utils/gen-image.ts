import { saveImageToFile } from "./same-image.ts";
import path from "path";
import { open } from "fs";
import { openai } from "@config/openai.ts";
import { env } from "./env.ts";


export const handleImageResponse = async (response: any, prompt: string) => {
  const outputDir = process.env.OUTPUT_DIR ?? "";
  
  if (response.data && Array.isArray(response.data) && response.data.length > 0) {
    const safePromptBase = prompt
      .replace(/[^a-zA-Z0-9]/g, '-')
      .substring(0, 80); // Keep room for index to avoid long filenames

    const savedPaths: string[] = [];

    for (let i = 0; i < response.data.length; i++) {
      const image = response.data[i];
      
      if (!image?.b64_json) continue;

      const filename = `${safePromptBase}_${i + 1}.png`;
      const filePath = path.join(outputDir, filename);
      
      await saveImageToFile(image.b64_json, filePath);
      console.log(`Image ${i + 1} saved to: ${filePath}`);
      savedPaths.push(filePath);
    }

    return savedPaths;
  } else {
    throw new Error('No image data found in the API response');
  }
};

export async function generateImage(prompt: string,N:number,seed:number): Promise<String | void> {
  try {
    
    const response = await openai.images.generate({
      prompt,    // The text prompt for image generation
      // model: "playground-v2-1024px-aesthetic",
      model: "fireworks::accounts/fireworks/models/playground-v2-5-1024px-aesthetic",
      // model: "fireworks::accounts/yi-01-ai/models/yi-large"

      // model: "fireworks::accounts/fireworks/models/playground-v2-5-1024px-aesthetic"
      n: N,
      // size: "1024x1024", // Image resolution (can be 256x256, 512x512, or 1024x1024)
    });

    console.log(response);

    await handleImageResponse(response, prompt)

    
    // console.log("Generated Image URL:", response.data[0].url);
  } catch (error) {
    console.error("Error generating image:", error);
  }
}

// Example usage

async function main(){  
  
  const prompt = "A futuristic cityscape with flying cars and neon lights";
  
  console.log("Prompt : "+prompt)
  // await generateImage(prompt,1);



}

// main()