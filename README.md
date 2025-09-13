# 🏋️ Fitness Regime Hub - Jekyll Website

A modern, user-friendly fitness and health website built with Jekyll for easy content management.

## 🚀 Quick Start Guide

### For Non-Developers: Simple 3-Step Publishing

1. **Create a new post** using the simple script
2. **Edit the content** with your fitness expertise  
3. **Commit and push** to GitHub to publish automatically

That's it! Your post is live on your website.

## 📝 Creating New Posts (Super Easy!)

### Method 1: Using the Python Script (Recommended)
```bash
python scripts/newpost.py
```

The script will ask you:
- Post title
- Description  
- Category (choose from list)
- Date (defaults to today)
- Featured image (optional)
- Tags (optional)

### Method 2: Create directly on GitHub (No scripts)
1. Go to your repo → `_posts` → Add file → Create new file
2. Name it `your-post-title.md`
3. Paste the template below and fill it in

### Method 3: Manual Creation
1. Create a new file in `_posts/` folder
2. Name it: `your-post-title.md` (no dates needed!)
3. Copy this template:

```markdown
---
layout: post
title: "Your Post Title"
description: "Brief description of your post"
categories: [Fitness]
date: 2024-01-15
image: /assets/images/your-image.jpg
tags: ["tag1", "tag2"]
---

# Your Post Title

Your content goes here...
```

## 📁 Project Structure

```
fitness-regime-hub/
├── _posts/                 # Your blog posts (add new ones here)
├── _layouts/               # Page templates (don't modify)
├── assets/
│   ├── css/               # Styling files
│   ├── js/                # JavaScript files  
│   └── images/            # Upload your images here
├── blog/                  # Blog index page
├── scripts/               # Post creation tools
├── _config.yml            # Site settings
└── index.html             # Homepage
```

## 🖼️ Adding Images

1. Save your images in `/assets/images/`
2. Use SEO-friendly names: `yoga-benefits.jpg`, `nutrition-tips.png`
3. Reference in posts: `![Alt text](/assets/images/your-image.jpg)`
4. Add as featured image: `image: /assets/images/your-image.jpg` in front matter

## 🏷️ Categories and Tags

### Available Categories:
- Fitness
- [Nutrition](https://fithealthregimen.com/category/nutrition-diet/)  
- Wellness
- Workouts
- Weight Loss
- Muscle Building
- Cardio
- Mental Health

### Using Tags:
Add relevant tags to help users find content:
```yaml
tags: ["yoga", "flexibility", "beginners", "stress relief"]
```

## 🌐 Publishing Your Changes

After creating or editing content:

```bash
git add .
git commit -m "Add new post: Your Post Title"  
git push origin main
```

Your changes will be live on your website within a few minutes!

## 🎯 SEO Best Practices (Built-in)

The website automatically handles:
- ✅ SEO-friendly URLs (no dates): `/benefits-of-yoga/`
- ✅ Meta descriptions from your post descriptions
- ✅ Proper heading structure (H1, H2, H3)
- ✅ Social media sharing
- ✅ Sitemap generation
- ✅ Fast loading times

## 📱 What's Included

### Features:
- **Responsive Design**: Looks great on all devices
- **Search Functionality**: Users can search your content  
- **Category Filtering**: Organize content by topic
- **Social Sharing**: Easy sharing buttons
- **Newsletter Signup**: Collect subscriber emails
- **Related Posts**: Keep users engaged
- **Fast Loading**: Optimized for speed

### Pages:
- Homepage with hero section
- Blog index with search and filtering
- Individual post pages with sharing
- Calculator pages (ready for your fitness tools)
- Contact page
- About page

## 🛠️ Customization

### Changing Site Information:
Edit `_config.yml`:
```yaml
title: "Your Site Name"
description: "Your site description"  
author:
  name: "Your Name"
  email: "your@email.com"
```

### Changing Colors/Styling:
Edit `/assets/css/main.css` and look for:
```css
:root {
  --primary-color: #006d5b;    /* Main color */
  --secondary-color: #ff914d;  /* Accent color */
  /* ... other colors */
}
```

### Adding New Pages:
1. Create a new `.html` or `.md` file
2. Add front matter:
```yaml
---
layout: default
title: "Page Title"
permalink: /page-url/
---
```

## 🔧 Local Development (Optional)

If you want to preview changes locally:

1. Install Jekyll:
```bash
gem install bundler jekyll
```

2. Install dependencies:
```bash
bundle install
```

3. Run local server:
```bash
bundle exec jekyll serve
```

4. View at: `http://localhost:4000`

## 📊 Analytics & Monitoring

### Adding Google Analytics:
1. Get your GA4 measurement ID
2. Add to `_config.yml`:
```yaml
google_analytics: GA_MEASUREMENT_ID
```

### Monitoring Performance:
- Use Google Search Console
- Check Core Web Vitals
- Monitor site speed with PageSpeed Insights

## 🆘 Troubleshooting

### Common Issues:

**Post not showing up?**
- Check the date isn't in the future
- Ensure proper front matter format
- Verify the file is in `_posts/` folder

**Images not loading?**
- Check file path: `/assets/images/filename.jpg`
- Ensure image file is uploaded to GitHub
- Use web-friendly formats: JPG, PNG, WebP

**Site not updating?**
- Check GitHub Actions tab for build errors
- Wait 2-3 minutes for changes to deploy
- Clear browser cache

## 📞 Getting Help

### Resources:
- Jekyll Documentation: https://jekyllrb.com/docs/
- Markdown Guide: https://www.markdownguide.org/
- GitHub Pages: https://pages.github.com/

### Quick Tips:
- Always test locally before pushing to main
- Keep image files under 500KB for fast loading
- Use descriptive filenames for SEO
- Write compelling meta descriptions (150-160 characters)

## 🎉 You're All Set!

Your website is now ready for easy content management. Focus on creating great fitness content—the technical stuff is handled automatically!

### Next Steps:
1. Create your first post using the script
2. Add some images to `/assets/images/`
3. Customize your About page
4. Set up Google Analytics
5. Start publishing amazing fitness content!

---


**Need help?** The post creation scripts guide you through everything, and this README covers all the basics. Happy writing! 💪
