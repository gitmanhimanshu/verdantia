# Vercel Deployment Guide

## Prerequisites
1. Install Vercel CLI: `npm install -g vercel`
2. Login to Vercel: `vercel login`

## Deployment Steps

### Option 1: Deploy via CLI
```bash
# Navigate to backend directory
cd verdantia/backend

# Deploy to Vercel
vercel --prod
```

### Option 2: Deploy via Dashboard
1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Set Root Directory to `backend`
5. Vercel will auto-detect Python

## Environment Variables
Set these in Vercel dashboard (Settings → Environment Variables):

```
MONGO_URI=your_mongodb_atlas_connection_string
JWT_SECRET_KEY=your_super_secret_jwt_key_here
FLASK_DEBUG=false
```

## Important Notes
- Vercel has a 10-second timeout on free plan
- Each request may have a cold start
- No persistent local storage (use cloud storage for files)
- MongoDB connections are optimized for serverless

## Testing
After deployment, test these endpoints:
- `https://your-app.vercel.app/` - API info
- `https://your-app.vercel.app/health` - Health check
- `https://your-app.vercel.app/api/auth/...` - Auth endpoints
