import { Command } from 'commander';
import { generateImage } from './utils/gen-image';

const program = new Command();

program
  .name('nearai')
  .description('NEAR AI Image Generation CLI')
  .version('1.0.0');

program
  .command('generate')
  .description('Generate an image from a text prompt')
  .argument('<prompt>', 'Text prompt for image generation')
  .option('-s, --size <size>', 'Image size (256x256, 512x512, or 1024x1024)', '1024x1024')
  .option('-n, --number <number>', 'Number of images to generate', '1')
  .action(async (prompt, options) => {
    try {
      console.log('🎨 Generating image with prompt:', prompt);
      const filePath = await generateImage(prompt);
      if (filePath) {
        console.log('✨ Image generated successfully at:', filePath);
      }
    } catch (error) {
      console.error('❌ Error:', error.message);
    }
  });

program.parse();