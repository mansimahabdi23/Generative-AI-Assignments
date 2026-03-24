<<<<<<< HEAD
# 🎨 Creative Artwork Generation using Stable Diffusion

## 📌 Project Overview

This project demonstrates the use of **Stable Diffusion**, a state-of-the-art text-to-image generative model, to create creative and high-quality artwork based on textual prompts. The implementation was carried out using **Google Colab** with GPU support as part of a **Generative AI / Diffusion Models assignment**.

Due to limitations in directly rendering executed Google Colab notebooks on GitHub, the outputs of the notebook are presented here using **generated image screenshots**.

---

## 🧠 What is Stable Diffusion?

Stable Diffusion is a **latent diffusion model** that generates images from text prompts. Instead of operating directly on pixel space, it performs the diffusion process in a compressed **latent space**, making it computationally efficient while maintaining image quality.

Key components include:

* CLIP Text Encoder
* Latent U-Net
* Scheduler
* Variational Autoencoder (VAE)

---

## 🎯 Problem Statement

Creating digital artwork manually is time-consuming and requires artistic skills. There is a need for an automated system that can generate visually appealing images efficiently using natural language descriptions.

---

## 💡 Proposed Solution

We use a **pre-trained Stable Diffusion v1.5 model** to generate creative artwork from text prompts. The model takes a user-defined prompt and produces a high-resolution image without requiring any additional training.

---

## ⚙️ System Workflow

1. User provides a text prompt
2. Text is converted into embeddings using CLIP
3. Random Gaussian noise is generated in latent space
4. U-Net progressively removes noise based on text conditioning
5. Scheduler controls the denoising steps
6. VAE decodes latent representation into a final image

---

## 🏗️ Architecture Used

The architecture consists of:

* **Frozen CLIP Text Encoder** – Converts text to embeddings
* **Latent U-Net** – Core denoising network
* **Scheduler** – Controls diffusion steps
* **VAE Decoder** – Converts latent output to image

(Architecture diagram included in the presentation)

---

## 🧪 Implementation Details

* Platform: Google Colab
* Language: Python
* Library: Hugging Face Diffusers
* Model: Stable Diffusion v1.5
* Hardware: GPU (Colab)

---

## 🖼️ Generated Outputs

Below are some example outputs generated using Stable Diffusion:

### 🔹 Example 1: Traditional Indian Village Festival

<img width="512" height="512" alt="Image" src="https://github.com/user-attachments/assets/fc00790a-f9f4-43dc-9381-ff9517491fe1" />

### 🔹 Example 2: Radha Krishna on Swing (Creative Prompt)

<img width="512" height="512" alt="Image" src="https://github.com/user-attachments/assets/960c6cc8-2394-4f8c-b247-5ba1d353c32b" />

### 🔹 Example 3: A futuristic cyberpunk Mumbai city, neon lights, ultra realistic, 4K

<img width="512" height="512" alt="Image" src="https://github.com/user-attachments/assets/d6434ad7-bc35-46a9-ab94-6604f4a1e678" />

> Note: Images are added as screenshots from the executed Google Colab notebook.



## 🔗 Google Colab Notebook

The implementation notebook was executed on Google Colab.

📎 **Colab Link:** https://colab.research.google.com/drive/13SxORY0j6GTDCYG0b1X48jVRu_m8AOxm#scrollTo=ozHH1_M3qJ_h

---

##  Conclusion

This project successfully demonstrates how Stable Diffusion can be used to generate creative artwork using text prompts. Pre-trained diffusion models provide an efficient and powerful approach to content generation in Generative AI applications.

---

##  Acknowledgment

This project was completed as part of an academic assignment on **Generative AI and Diffusion Models**.

---

## 👩‍💻 Author

**Name:** [Your Name]
=======
# 🎨 Creative Artwork Generation using Stable Diffusion

## 📌 Project Overview

This project demonstrates the use of **Stable Diffusion**, a state-of-the-art text-to-image generative model, to create creative and high-quality artwork based on textual prompts. The implementation was carried out using **Google Colab** with GPU support as part of a **Generative AI / Diffusion Models assignment**.

Due to limitations in directly rendering executed Google Colab notebooks on GitHub, the outputs of the notebook are presented here using **generated image screenshots**.

---

## 🧠 What is Stable Diffusion?

Stable Diffusion is a **latent diffusion model** that generates images from text prompts. Instead of operating directly on pixel space, it performs the diffusion process in a compressed **latent space**, making it computationally efficient while maintaining image quality.

Key components include:

* CLIP Text Encoder
* Latent U-Net
* Scheduler
* Variational Autoencoder (VAE)

---

## 🎯 Problem Statement

Creating digital artwork manually is time-consuming and requires artistic skills. There is a need for an automated system that can generate visually appealing images efficiently using natural language descriptions.

---

## 💡 Proposed Solution

We use a **pre-trained Stable Diffusion v1.5 model** to generate creative artwork from text prompts. The model takes a user-defined prompt and produces a high-resolution image without requiring any additional training.

---

## ⚙️ System Workflow

1. User provides a text prompt
2. Text is converted into embeddings using CLIP
3. Random Gaussian noise is generated in latent space
4. U-Net progressively removes noise based on text conditioning
5. Scheduler controls the denoising steps
6. VAE decodes latent representation into a final image

---

## 🏗️ Architecture Used

The architecture consists of:

* **Frozen CLIP Text Encoder** – Converts text to embeddings
* **Latent U-Net** – Core denoising network
* **Scheduler** – Controls diffusion steps
* **VAE Decoder** – Converts latent output to image

(Architecture diagram included in the presentation)

---

## 🧪 Implementation Details

* Platform: Google Colab
* Language: Python
* Library: Hugging Face Diffusers
* Model: Stable Diffusion v1.5
* Hardware: GPU (Colab)

---

## 🖼️ Generated Outputs

Below are some example outputs generated using Stable Diffusion:

### 🔹 Example 1: Traditional Indian Village Festival

<img width="512" height="512" alt="Image" src="https://github.com/user-attachments/assets/fc00790a-f9f4-43dc-9381-ff9517491fe1" />

### 🔹 Example 2: Radha Krishna on Swing (Creative Prompt)

<img width="512" height="512" alt="Image" src="https://github.com/user-attachments/assets/960c6cc8-2394-4f8c-b247-5ba1d353c32b" />

### 🔹 Example 3: A futuristic cyberpunk Mumbai city, neon lights, ultra realistic, 4K

<img width="512" height="512" alt="Image" src="https://github.com/user-attachments/assets/d6434ad7-bc35-46a9-ab94-6604f4a1e678" />

> Note: Images are added as screenshots from the executed Google Colab notebook.



## 🔗 Google Colab Notebook

The implementation notebook was executed on Google Colab.

📎 **Colab Link:** https://colab.research.google.com/drive/13SxORY0j6GTDCYG0b1X48jVRu_m8AOxm#scrollTo=ozHH1_M3qJ_h

---

##  Conclusion

This project successfully demonstrates how Stable Diffusion can be used to generate creative artwork using text prompts. Pre-trained diffusion models provide an efficient and powerful approach to content generation in Generative AI applications.

---

##  Acknowledgment

This project was completed as part of an academic assignment on **Generative AI and Diffusion Models**.

---

## 👩‍💻 Author

**Name:** [Your Name]
>>>>>>> 9800705bd95af3ee9e6d1ef93613bafea4bd054c
