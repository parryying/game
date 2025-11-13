# Game Website

A simple website displaying the word "game" in green font.

## Local Development

### Option 1: Python Server
Run the included Python server:
```bash
python server.py
```
Then open your browser to `http://localhost:8000`

### Option 2: Using Python's built-in server
```bash
python -m http.server 8000
```

### Option 3: Using Node.js (if you have it installed)
```bash
npx serve .
```

## Public Deployment Options

### 1. GitHub Pages (Free)
1. Push this repository to GitHub
2. Go to repository Settings → Pages
3. Set source to "Deploy from a branch" and select `main` branch
4. Your site will be available at `https://yourusername.github.io/repositoryname`

### 2. Netlify (Free)
1. Create account at [netlify.com](https://netlify.com)
2. Drag and drop the project folder to Netlify dashboard
3. Your site will get a random URL like `https://random-name.netlify.app`

### 3. Vercel (Free)
1. Create account at [vercel.com](https://vercel.com)
2. Connect your GitHub repository
3. Deploy with one click

### 4. Firebase Hosting (Free)
1. Install Firebase CLI: `npm install -g firebase-tools`
2. Run `firebase init hosting`
3. Run `firebase deploy`

### 5. Surge.sh (Free)
1. Install: `npm install -g surge`
2. Run `surge` in the project directory
3. Follow the prompts

## Files

- `index.html` - Main website file with green "game" text
- `server.py` - Local Python development server
- `README.md` - This file

## Features

- Responsive design
- Green animated "game" text
- Simple and clean layout
- Cross-browser compatible