## 项目结构

- prompt: 基于提示工程为LLM提供trace
  - datasets: 存放数据集文件
  - apichat.py: 主程序用于与LLM进行交互
  - intermediate.py: 提供一个python程序的trace
  - results.csv: 存放结果
- finetune: 微调中小模型实现为模型提供trace
  - codellama.py: codellama模型程序运行程序
  - results.csv: 存放结果
  - utils.py: 提供一些工具函数