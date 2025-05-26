import { Command } from 'commander';
import { generateImage } from '@utils/gen-image.ts';

const program = new Command();

const IMAGE_PROMPT =env("PROMPT",'A pair of clear hands looking through a transparent glass Christmas ball,hyper-realistic, minimalist, futuristic background with cute Christmas decorations like Santa Claus, a snowman, and snowflakes, 8k')


import {config} from "dotenv"
import { env } from '@utils/env.ts';

config()

program
  .name('nearai')
  .description('NEAR AI Image Generation CLI')
  .version('1.0.0');

program
  .command('generate')
  .description('Generate an image from a text prompt')
  .option('-p, --prompt <string>', 'Prompt to generate image', IMAGE_PROMPT )
  .option('-s, --size <size>', 'Image size (256x256, 512x512, or 1024x1024)', '1024x1024')
  .option('-n, --number <number>', 'Number of images to generate',  env("NUM_IMAGES",'1'))
  .action(async ({prompt, number}) => {
    try {
      console.log('🎨 Generating image with prompt:', prompt);
      const filePath = await generateImage(prompt,number);
      if (filePath) {
        console.log('✨ Image generated successfully at:', filePath);
      }
    } catch (error) {
      console.error('❌ Error:', error.message);
    }
  });

program.parse(process.argv);