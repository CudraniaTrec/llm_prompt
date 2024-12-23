## 项目结构

- prompt: 基于提示工程为LLM提供trace
  - datasets/: 存放数据集文件
  - apichat.py: 主程序用于与LLM进行交互
  - intermediate.py: 提供一个python程序的trace
  - results.csv: 存放结果
- finetune: 微调中小模型实现为模型提供trace
  - output/: 存放训练的模型与过程信息
  - tmp/: 存放一些临时的文件
  - wandb/: 存放wandb的信息
  - annotate.py: 用于接受trace信息并标注python程序
  - codellama.py: codellama模型，微调与运行程序
  - opencoder.py: opencoder,qwen模型，微调与运行程序
  - draw.ipynb: 用于绘制图片
  - results.csv: 存放结果
  - utils.py: 提供一些工具函数
  - trace.py: 执行python程序，生成trace提供给annotate.py