import { Command } from "commander"
import { generateImage, type DTOImageGenerate } from "@utils/gen-image.ts"

import { IMAGE_MODEL, IMAGE_PROMPT, SMART_MODEl } from "@config/index.ts"

const program = new Command()

import { config } from "dotenv"
import { env } from "@utils/env.ts"
import { genJoke, genSmartPrompt } from "@utils/gen-text.ts"
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
    "-N, --number <number>",
    "Number of images to generate",
    env("NUM_IMAGES", "1")
  )
  .option("-m, --model <string>", "Model used to generate image", IMAGE_MODEL)
  // .option('-r, --random <boolean>', 'Number of images to generate',  env("RANDOM_IMAGES",false))
  .option("--seed <number>", "Random Seed", env("RANDOM_SEED", `1`))
  .option("--steps <number>", "No of steps", process.env.STEPS)
  .action(async (dto:DTOImageGenerate) => {
    // const { prompt, number, seed, model } = dto
    try {
      console.log(
        `🎨 Generating with followiing configuration \n${JSON.stringify(dto, null, 2)}`
      )
      await generateImage(dto)
    } catch (error) {
      console.error("❌ Error:", error)
    }
  })

const JOKE_PROMPT = "Tell me a funny programmer joke."

program
  .command("joke")
  .description("Generate a joke using a witty AI model")
  .option("-p, --prompt <string>", "Prompt to generate a joke", JOKE_PROMPT)
  .option("-m, --model <string>", "Model to use", SMART_MODEl)
  .action(async ({ prompt, model }) => {
    try {
      console.log("🃏 Generating joke with prompt:", prompt)
      const joke = await genJoke(prompt, model)
      console.log("😂 Joke:", joke)
    } catch (error: any) {
      console.error("❌ Error:", error.message)
    }
  })

program
  .command("smartPrompt")
  .description("Generate smart prompt for ai creations")
  .option("-p, --prompt <string>", "Prompt", IMAGE_PROMPT)
  .option("-m, --model <string>", "Model", SMART_MODEl)
  .action(async ({ prompt, model }) => {
    try {
      console.log("🃏 Generating smart prompt for prompt:", prompt)
      const smartPrompt = await genSmartPrompt({prompt, model})
      console.log("Smart Prompt:", smartPrompt)
    } catch (error: any) {
      console.error("❌ Error:", error.message)
    }
  })

program.parse(process.argv)
