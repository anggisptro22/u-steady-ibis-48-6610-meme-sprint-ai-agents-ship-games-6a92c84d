import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const memePath = path.join(__dirname, 'meme.png');
const outputDir = '/output';
const outputPath = path.join(outputDir, 'entry.png');

if (!fs.existsSync(memePath)) {
  throw new Error(`Error: Required file "${memePath}" is missing.`);
}

fs.mkdirSync(outputDir, { recursive: true });
fs.copyFileSync(memePath, outputPath);
