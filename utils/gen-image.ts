import OpenAI from "openai";
import { saveImageToFile } from "./same-image.ts";
import path from "path";



const auth =  {
        "account_id": "hirocoin.near",
        "signature": "syCVwqm03oTk5CTHc/btmNX4Rtb59VTV8r3pmSniSFyY98t0oqLY7FLC8QWlPPzv4pbm7crdxc49MwHH2bNMBA==",
        "public_key": "ed25519:GSawU7vtBcUCq3m9VyETsp9xzUz1L5XBf9H4JkdngfyX",
        "callback_url": "http://localhost:63580/capture",
        "nonce": "1744849079161",
        "recipient": "ai.near",
        "message": "Welcome to NEAR AI",
        "on_behalf_of": null
  }


process.env.OPENAI_BASE_URL = "https://api.near.ai/v1"; // Set the base URL for the OpenAI API
process.env.OPENAI_API_KEY = `Bearer ${JSON.stringify(auth)}`


export const initializeOpenAI = (auth: any) => {
  process.env.OPENAI_BASE_URL = "https://api.near.ai/v1";
  process.env.OPENAI_API_KEY = `Bearer ${JSON.stringify(auth)}`;
  return new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
  });
};

export async function generateImage(prompt: string, openaiInstance?: OpenAI): Promise<String | void> {
  const openai = openaiInstance || initializeOpenAI(auth);
  try {
    const response = await openai.images.generate({
      prompt: prompt,    // The text prompt for image generation
      // n: 1,              // Number of images to generate
      // size: "1024x1024", // Image resolution (can be 256x256, 512x512, or 1024x1024)
    });

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
  await generateImage(prompt);
}

// main()