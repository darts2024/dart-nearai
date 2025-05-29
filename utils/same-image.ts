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

export async function getImageBase64(imagePath: string): Promise<string> {
  const resolvedPath = path.resolve(imagePath);
  const imageBuffer = await fs.promises.readFile(resolvedPath);
  
  const mimeType = getMimeType(resolvedPath);

  // return imageBuffer.toString('base64')
  return `data:${mimeType};base64,${imageBuffer.toString('base64')}`;

}


function getMimeType(filePath: string): string {
  const ext = path.extname(filePath).toLowerCase();
  switch (ext) {
    case '.jpg':
    case '.jpeg':
      return 'image/jpeg';
    case '.png':
      return 'image/png';
    case '.gif':
      return 'image/gif';
    case '.webp':
      return 'image/webp';
    case '.svg':
      return 'image/svg+xml';
    default:
      return 'application/octet-stream';
  }
}