import { saveImageToFile } from "./same-image.ts";
import path from "path";
import { open } from "fs";
import { openai } from "@config/openai.ts";



export async function generateImage(prompt: string,N:number): Promise<String | void> {
  try {
    
    const response = await openai.images.generate({
      prompt: prompt,    // The text prompt for image generation
      n: N,
      // seed: 400000,
      // model: "stable-diffusion-3",
      // n: 1,              // Number of images to generate
      // size: "1024x1024", // Image resolution (can be 256x256, 512x512, or 1024x1024)
    });

    console.log(response);

    if (response.data && response.data[0] && response.data[0].b64_json) {
      let outputDir = process.env.OUTPUT_DIR ?? ""

      // Create a safe filename from the prompt
      const safePrompt = prompt
        .replace(/[^a-zA-Z0-9]/g, '_') // Replace non-alphanumeric chars with underscore
        .substring(0, 100); // Limit length to avoid extremely long filenames
      
      const filename = `${safePrompt}.png`;

      const filePath = path.join(outputDir, filename);
      
      await saveImageToFile(response.data[0].b64_json, filePath);
      
      console.log(`Image successfully saved to: ${filePath}`);
      return filePath;
    } else {
      throw new Error('No image data found in the API response');
    }
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