from transformers import AutoModelForCausalLM, AutoTokenizer

# Загружаем модель StarCoder
model_name = "bigcode/starcoder"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_code(prompt):
    try:
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=150)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        return f"Ошибка генерации кода: {e}"

# Пример использования
if __name__ == "__main__":
    prompt = "Напиши код на Python для клика по элементу с использованием Selenium."
    generated_code = generate_code(prompt)
    print(generated_code)