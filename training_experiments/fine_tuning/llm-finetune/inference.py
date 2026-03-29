from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "outputs/qwen2"  # or full path to llm-finetune/outputs/qwen2
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)
# Example: instruction-style prompt (match how your data was formatted)
prompt = '''### Instruction:
What is the API rate limit?
### Response:'''
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=128)
print(f"output: {tokenizer.decode(outputs[0], skip_special_tokens=True)}")
