# AI Evaluation Project (Starter)


This repository showcases a lightweight evaluation framework for comparing AI model responses.  
The goal is to test models side by side, apply consistent rubrics, and surface meaningful insights.  

---

## 📂 What’s Inside  

- **prompts/** → contains the exact test prompts (one file per prompt).  
- **responses/<model>/** → raw outputs from each model (GPT, Claude, Gemini), matched to prompt filenames.  
- **evaluations/** → rubric details, scoring results, and analysis reports.  
- **scripts/** → helper tools for scoring or formatting.  
- **notebooks/** → optional Jupyter notebooks for extended analysis or visualization.  

---

## 🚀 Quick Start  

1. Add test prompts in **prompts/**.  
2. Collect outputs for each model and save them in **responses/<model>/** with consistent filenames.  
3. Score the responses using the rubric in **evaluations/rubric.md**.  
4. Log results in **evaluations/scored_results.csv**.  
5. Summarize findings in **evaluations/analysis.md**.  

---

## 📊 Project Overview  

In this project, I tested **two prompts** across **three AI models** (*GPT-5, Claude Sonnet-4, Gemini 2.5 Flash*).  
Each response was evaluated on **eight rubric dimensions**, scored systematically, and then compared.  

The analysis highlights:  
- Which models excelled in clarity, completeness, and truthfulness.  
- Where some models matched equally strong performance.  
- Where others stood out by showing qualities like **follow-up engagement** and **rapport-building**.  

This study demonstrates how even small, structured evaluations can uncover practical differences in model behavior, guiding better model selection for real-world use cases.  

---
