#!/usr/bin/env python3
"""
Simple Post Generator for Fitness Regime Hub
Usage: python scripts/newpost.py
"""

import os
import sys
from datetime import datetime
import re

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def get_user_input():
    """Get post information from user"""
    print("🏋️ Fitness Regime Hub - New Post Generator")
    print("=" * 50)
    
    title = input("📝 Post title: ").strip()
    if not title:
        print("❌ Title is required!")
        sys.exit(1)
    
    description = input("📄 Description: ").strip()
    if not description:
        description = f"Learn about {title.lower()} with expert tips and guidance from Fitness Regime Hub."
    
    print("\n📂 Available categories:")
    categories = ["Fitness", "Nutrition", "Wellness", "Workouts", "Weight Loss", "Muscle Building", "Cardio", "Mental Health"]
    for i, cat in enumerate(categories, 1):
        print(f"   {i}. {cat}")
    
    print("   0. Custom category")
    
    cat_choice = input("\n🏷️ Select category (1-8, or 0 for custom): ").strip()
    
    if cat_choice == "0":
        category = input("📝 Enter custom category: ").strip()
        if not category:
            category = "Fitness"
    elif cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
        category = categories[int(cat_choice) - 1]
    else:
        category = "Fitness"
    
    # Date input
    date_input = input(f"📅 Date (YYYY-MM-DD, default: {datetime.now().strftime('%Y-%m-%d')}): ").strip()
    if not date_input:
        date_input = datetime.now().strftime('%Y-%m-%d')
    
    try:
        datetime.strptime(date_input, '%Y-%m-%d')
    except ValueError:
        print("❌ Invalid date format! Using today's date.")
        date_input = datetime.now().strftime('%Y-%m-%d')
    
    # Optional image
    image_input = input("🖼️ Featured image filename (optional, in /assets/images/): ").strip()
    image_path = f"/assets/images/{image_input}" if image_input else ""
    
    # Optional tags
    tags_input = input("🏷️ Tags (comma-separated, optional): ").strip()
    tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()] if tags_input else []
    
    return {
        'title': title,
        'description': description,
        'category': category,
        'date': date_input,
        'image': image_path,
        'tags': tags
    }

def create_post_file(post_data):
    """Create the markdown post file"""
    slug = slugify(post_data['title'])
    filename = f"{slug}.md"
    filepath = os.path.join("_posts", filename)
    
    # Ensure _posts directory exists
    os.makedirs("_posts", exist_ok=True)
    
    # Check if file already exists
    if os.path.exists(filepath):
        overwrite = input(f"⚠️ File '{filename}' already exists. Overwrite? (y/N): ").strip().lower()
        if overwrite != 'y':
            print("❌ Cancelled. File not created.")
            return None
    
    # Create front matter
    front_matter = f"""---
layout: post
title: "{post_data['title']}"
description: "{post_data['description']}"
categories: [{post_data['category']}]
date: {post_data['date']}"""
    
    if post_data['image']:
        front_matter += f'\nimage: {post_data["image"]}'
    
    if post_data['tags']:
        tags_str = ', '.join([f'"{tag}"' for tag in post_data['tags']])
        front_matter += f'\ntags: [{tags_str}]'
    
    front_matter += "\n---\n\n"
    
    # Create post content template
    content = f"""# {post_data['title']}

{post_data['description']}

## Introduction

Write your introduction here. Explain what readers will learn and why this topic is important for their fitness journey.

## Main Content

### Section 1: Getting Started

Add your main content here. Include practical tips, step-by-step instructions, or detailed explanations.

### Section 2: Key Points

- **Point 1**: Explain the first important concept
- **Point 2**: Describe the second key idea
- **Point 3**: Share the third essential tip

### Section 3: Practical Application

Provide actionable advice that readers can implement immediately:

1. **Step 1**: First action to take
2. **Step 2**: Second step in the process
3. **Step 3**: Final step for success

## Expert Tips

💡 **Pro Tip**: Share a valuable insight from fitness professionals.

⚠️ **Important**: Highlight any safety considerations or precautions.

✅ **Remember**: Remind readers of key takeaways.

## Common Mistakes to Avoid

- Mistake 1 and how to avoid it
- Mistake 2 and better alternatives
- Mistake 3 and prevention strategies

## Conclusion

Summarize the main points and encourage readers to take action. Include a call-to-action that relates to your fitness services or other helpful content.

## Related Resources

- [Link to related post 1](#)
- [Link to related post 2](#)
- [Link to relevant calculator](/calculators/)

---

*Need personalized fitness guidance? Check out our [fitness calculators](/calculators/) or [contact us](/contact/) for expert advice tailored to your goals.*
"""
    
    # Write the file
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(front_matter + content)
        
        print(f"✅ Success! Post created: {filepath}")
        print(f"\n📝 Next steps:")
        print(f"   1. Edit the content in {filepath}")
        print(f"   2. Add your featured image to /assets/images/ (if specified)")
        print(f"   3. Commit and push to GitHub:")
        print(f"      git add {filepath}")
        print(f"      git commit -m 'Add new post: {post_data['title']}'")
        print(f"      git push origin main")
        print(f"\n🌐 URL will be: /{slug}/")
        
        return filepath
        
    except Exception as e:
        print(f"❌ Error creating file: {e}")
        return None

def main():
    """Main function"""
    try:
        post_data = get_user_input()
        filepath = create_post_file(post_data)
        
        if filepath:
            print(f"\n🎉 Post generator completed successfully!")
        
    except KeyboardInterrupt:
        print("\n\n👋 Cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
