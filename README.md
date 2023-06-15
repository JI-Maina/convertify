# Convertify
![Convertify landing page image](/app/static/Convertify.png)

# Introduction
### The Project
Convertify is a three-fold image manipulation tool that effortlessly resizes, compresses and converts image formats unleashing the full potential of visual content. It is designed to serve most if not all social media users, photographers, and editors. With one click a user can easily convert an image into another format, resize it or better compress it to a smaller size without losing quality.

### The Context
Before I transitioned into software engineering I was and still am a trained journalist. Most of my work is spent on the production side of journalism where I deal with editing be it images or videos. But there have been nugging issues with the raw size of footage, especially with images. And as such i decided to come up with an image manupilation site as my portfolio project, concluding Foundations as ALX School.

### The Team
I worked on the project alone. You can follow me on [twitter](https://twitter.com/Johnskjaer) or [Linkedin](https://www.linkedin.com/in/john-maina-679869188/).

### Blog Post
After the development phase, I wrote a blog post shairing my experience:
- Convertify: [Lessons Learnt and Whole Experience Designing my First Project](https://medium.com/@irungujmaina/convertify-enhance-your-images-lessons-learnt-and-whole-experience-designing-my-first-project-6e893a2c538f)

## Installation
The project is not yet deployed but you can use it locally on your machine by following below installation steps:
1. Clone the repository
    - git clone https://github.com/JI-Maina/convertify.git
2. Make a virtual environment
    - python3 -m venv .venv
4. Activate virtual environment
    - source .venv/bin/activate
5. Install dependancies
    - pip install -r requirements.txt
6. Run app
    - python run.py
7. Enjoy convertify on the browser
    - visit https://127.0.0.1:5000/

## Usage
After you navigate to one of the pages (resize, convert or compress), you need to first of all upload an image.
![Convertify landing page image](/app/static/Convertify.png)
Then you can click the button on the respective pages.However on the convert page, you need to chose a convert operation before proceeding with the convert button.
![Convertify - upload image form](/app/static/upload-convert.png)
After the operation is done on the uploaded image, the original image and new image will be displayed. On top of the manipulated image will be a download button. You can click it to get your modified image.
![Convertify - download manipulated image](/app/static/download-converted.png)

## Contribution
John Maina is the only contributor at this time.

## Related projects
- [webp2jpg-online](https://github.com/renzhezhilu/webp2jpg-online)
- [Converseen](https://github.com/Faster3ck/Converseen)

## Licesing
Free to use but please give me credit.