# 🚀 Render Deployment Guide

## Files Created for Render Deployment

### 1. `requirements.txt` ✅
- Updated with `certifi==2025.10.5`
- All dependencies specified with exact versions

### 2. `Procfile` ✅
```
web: gunicorn app:app
```

### 3. `render.yaml` ✅
- Configured for Python 3.11
- Free tier plan
- Proper build and start commands

### 4. `app.py` ✅
- Updated for production environment
- Uses PORT environment variable
- Debug mode disabled by default

## 🚀 Deployment Steps

### Step 1: Push to GitHub
```bash
cd verdantia
git add .
git commit -m "Prepare backend for Render deployment"
git push origin main
```

### Step 2: Deploy on Render

#### Option A: Via Render Dashboard
1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: `verdantia-backend`
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

#### Option B: Via Render CLI
```bash
# Install Render CLI
npm install -g @render/cli

# Login and deploy
render login
render deploy
```

### Step 3: Environment Variables
Add these in Render dashboard → Environment:

**Required:**
```
MONGO_URI=your_mongodb_atlas_connection_string
JWT_SECRET_KEY=your_super_secret_jwt_key_here
```

**Optional:**
```
MONGO_DB=verdantia
FLASK_DEBUG=false
CORS_ORIGINS=*
UPLOAD_DIR=uploads
CERT_DIR=certs
```

### Step 4: Test Deployment
1. Check Render logs for any errors
2. Visit your service URL
3. Test health endpoint: `https://your-app.onrender.com/health`
4. Test API endpoints

## 🔧 Configuration Details

### MongoDB Atlas Setup
- Ensure your MongoDB Atlas cluster allows connections from all IPs (0.0.0.0/0)
- Create a database user with read/write permissions
- Use connection string format: `mongodb+srv://username:password@cluster.mongodb.net/verdantia?retryWrites=true&w=majority`

### CORS Configuration
- Already configured to allow all origins (`*`)
- Supports credentials
- Handles all HTTP methods

### Production Settings
- Debug mode disabled by default
- Uses Gunicorn WSGI server
- Proper error handling
- Health check endpoint available

## 📊 Monitoring
- Check Render dashboard for deployment status
- Monitor logs for runtime errors
- Test all API endpoints after deployment

## 🔗 Frontend Integration
Update your frontend API base URL to point to your Render backend:
```javascript
const API_BASE_URL = 'https://your-backend-app.onrender.com';
```

Your backend is now ready for deployment on Render!
