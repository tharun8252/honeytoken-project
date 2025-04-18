# Honeytoken Generation and Monitoring System using LLM

## Overview

This project presents a novel system for generating and monitoring honeytokens using a fine-tuned lightweight language model (DistilGPT2). Honeytokens—fake but realistic credentials such as API keys, passwords, or emails—serve as effective tools for detecting unauthorized access and insider threats. This system not only automates honeytoken generation using machine learning but also integrates with Splunk for real-time threat monitoring.

## Key Features

- **Structured Honeytoken Generation**  
  Generates realistic decoy credentials using fine-tuned LLMs trained on a synthetic but context-rich dataset.

- **Lightweight Fine-tuned Model (DistilGPT2)**  
  Leverages Hugging Face's `transformers` library for training and inference, optimizing for low memory usage and high performance.

- **Real-time Monitoring via Splunk Cloud**  
  Logs honeytoken activity to Splunk HEC, allowing visualization and alerting through the Splunk UI.

- **Secure Communications**  
  Includes certificate management and secure HTTPS connectivity to Splunk Cloud.

## Technologies Used

- Python
- Hugging Face Transformers (DistilGPT2)
- PyTorch
- Splunk Cloud (HEC)
- Datasets (Hugging Face)
- OpenSSL (Certificate Handling)
- Requests (REST API)
- Google Colab / Jupyter Notebook
- Pandas

## Project Structure

```bash
honeytoken_project/
│
├── data_preprocessing.py           # Cleans and merges raw credential datasets
├── format_for_training.py          # Formats structured data into LLM-ready text
├── train_gpt2.py                   # Fine-tunes DistilGPT2
├── save_model.py                   # Persists the fine-tuned model and tokenizer
├── load_model.py                   # Loads model for generation
├── splunk_cert_setup.py            # Installs Splunk certificates securely
├── test_splunk_connection.py       # Validates logging connectivity
├── generate_honeytoken.py          # Generates and logs honeytoken to Splunk
├── formatted_honeytokens.txt       # Training-ready dataset
├── cleaned_honeytoken_dataset.csv  # Cleaned input dataset
├── fine_tuned_gpt2/                # Saved model artifacts
└── README.md
```

## Installation

Install required dependencies:

```bash
pip install pandas transformers datasets torch accelerate requests
```

Ensure your certificate paths and token configurations are correct in the relevant files.

## Usage

1. Run `data_preprocessing.py` to generate a cleaned dataset.
2. Format that dataset using `format_for_training.py`.
3. Fine-tune the model using `train_gpt2.py`.
4. Save the model with `save_model.py`, and load it later using `load_model.py`.
5. Set up certificate handling using `splunk_cert_setup.py` and validate with `test_splunk_connection.py`.
6. Generate and log honeytokens using `generate_honeytoken.py`.

## Application Areas

- Cyber Deception and Threat Detection
- Insider Threat Identification
- AI-based Anomaly Monitoring
- Honeypot-enhanced Monitoring Systems

## Future Work

- Add UI/dashboard for honeytoken generation and status visualization
- Extend support to multi-format honeytokens (PDF, QR, file-based)
- Deploy model via Flask or FastAPI for real-time API access
- Integrate threat intelligence feeds for adaptive response

## Version

**v1.0** – Initial version with model fine-tuning, Splunk integration, and SSL support.

## Citation

If you use this work in your research or security project, please cite:

```
@software{tharun_honeytoken_2025,
  author = {Tharun},
  title = {Honeytoken Generation and Monitoring using Fine-tuned DistilGPT2},
  year = {2025},
  url = {https://github.com/tharun8252/honeytoken-project}
}
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

**Tharun**  
M.Tech Cybersecurity, Amrita Vishwa Vidyapeetham  
[GitHub Profile](https://github.com/tharun8252)  
Email: tharun07man1ofcou@gmail.com