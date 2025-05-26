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


async function main() {
  console.log(await genJoke("Tell me a joke about developers"))
}

// main()