import * as fs from 'fs';
import * as path from 'path';

// Function to save base64 image to a file
export async function saveImageToFile(base64Image: string,filepath:string) {
  try {
    // Remove any potential data URL prefix if present
    const base64Data = base64Image.replace(/^data:image\/\w+;base64,/, '');
    
    // Create a buffer from the base64 data
    const buffer = Buffer.from(base64Data, 'base64');
        
    // Write the buffer to file
    await fs.promises.writeFile(filepath, buffer);
    
  } catch (error) {
    console.error('Error saving image to file:', error);
    throw error;
  }
}