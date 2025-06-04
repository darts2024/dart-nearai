import { Command } from "commander"
import { generateImage } from "@utils/gen-image.ts"

const program = new Command()

const IMAGE_PROMPT = env(
  "Prompt",
  "A pair of clear hands looking through a transparent glass Christmas ball,hyper-realistic, minimalist, futuristic background with cute Christmas decorations like Santa Claus, a snowman, and snowflakes, 8k"
)

import { config } from "dotenv"
import { env } from "@utils/env.ts"
import { genJoke } from "@utils/gen-text.ts"
import { getRandomInt } from "@utils/random.ts"

config()

program
  .name("nearai")
  .description("NEAR AI Image Generation CLI")
  .version("1.0.0")

program
  .command("generate")
  .description("Generate an image from a text prompt")
  .option("-p, --prompt <string>", "Prompt to generate image", IMAGE_PROMPT)
  .option(
    "-s, --size <size>",
    "Image size (256x256, 512x512, or 1024x1024)",
    "1024x1024"
  )
  .option(
    "-n, --number <number>",
    "Number of images to generate",
    env("NUM_IMAGES", "1")
  )
  // .option('-r, --random <boolean>', 'Number of images to generate',  env("RANDOM_IMAGES",false))
  .option("--seed <number>", "Random Seed", env("RANDOM_SEED", `1`))
  .action(async ({ prompt, number, seed }) => {
    try {
      console.log(`🎨 Generating ${number} image with prompt:`, prompt)
      await generateImage({ prompt, N: number, seed })
    } catch (error) {
      console.error("❌ Error:", error)
    }
  })

const DEFAULT_PROMPT = "Tell me a funny programmer joke."

program
  .command("joke")
  .description("Generate a joke using a witty AI model")
  .option("-p, --prompt <string>", "Prompt to generate a joke", DEFAULT_PROMPT)
  .option(
    "-m, --model <string>",
    "Model ID to use",
    "fireworks::accounts/fireworks/models/mixtral-8x22b-instruct"
  )
  .action(async ({ prompt, model }) => {
    try {
      console.log("🃏 Generating joke with prompt:", prompt)
      const joke = await genJoke(prompt, model)
      console.log("😂 Joke:", joke)
    } catch (error: any) {
      console.error("❌ Error:", error.message)
    }
  })

program.parse(process.argv)
