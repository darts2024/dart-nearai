import { openai } from "@config/openai.ts";

export async function genJoke(prompt: string,model:string="fireworks::accounts/fireworks/models/mixtral-8x22b-instruct"): Promise<string> {

  const response = await openai.chat.completions.create({
    model, 
    messages: [
      { role: "system", content: "You are a witty assistant that tells jokes." },
      { role: "user", content: prompt }
    ],
    temperature: 0.8, // Adjust for more creativity
    max_tokens: 100
  });

  return response.choices[0].message.content.trim();
}

export interface DTOText {
  prompt: string;
  model: string 
  imageModel?: string;
}




export async function genSmartPrompt(dto: DTOText): Promise<string> {
  const { model, prompt } = dto;
  
  const systemPrompt = `
  Transform user input into optimized image generation prompts with these components:
  1. Subject: Detailed description with adjectives
  2. Style: Art medium (digital art/photo/painting) + genre (cyberpunk/realism)
  3. Technical: 4k, ultra-detailed, studio lighting, depth of field
  4. Context: Intended use (wall art/logo/social media)
  
  Format: 
  "[Subject description], [art style], [technical specs], [contextual tags]"
  
  Example transformation:
  Input: "A space cat"
  Output: "A majestic silver-furred cat with glowing green eyes floating in zero gravity, 
          digital art, cyberpunk neon aesthetic, 8k resolution, ultra-detailed fur texture, 
          cinematic lighting, trending on ArtStation, for fantasy book cover"
  `;

  const response = await openai.chat.completions.create({
    model,
    messages: [
      { 
        role: "system", 
        content: systemPrompt 
      },
      { 
        role: "user", 
        content: `Original prompt: ${prompt}`
      }
    ],
    temperature: 0.7, // Balances creativity and consistency
    max_tokens: 150
  });

  return formatPrompt(response.choices[0].message.content.trim());
}

function formatPrompt(rawText: string): string {
  // Add validation and fallback logic here
  return rawText.replace(/, +/g, ', '); // Normalize spacing
}





async function main() {
  console.log(await genJoke("Tell me a joke about developers"))
}

// main()