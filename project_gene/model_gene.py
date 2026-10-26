from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

# 按模型训练时的顺序定义基因名称
GENE_NAMES = ["CD44", "CCL4", "TYROBP", "CCL5", "TNF", 
              "HLA-B", "HLA-DRA", "B2M", "HLA-DRB1", "HLA-A"]

@app.route('/')
def home():
    return render_template('index.html', gene_names=GENE_NAMES)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 获取表单数据并验证
        data = request.form.to_dict()
        
        # 按正确顺序创建输入数组
        input_data = np.array([
            [float(data[gene]) for gene in GENE_NAMES]
        ])
        
        # 获取预测概率
        prob_malignant = model.predict_proba(input_data)[0][1] * 100
        
        return render_template('index.html',
                            gene_names=GENE_NAMES,
                            probability=f"{prob_malignant:.1f}%")
    
    except ValueError as e:
        return render_template('index.html',
                            gene_names=GENE_NAMES,
                            error=f"输入错误: {str(e)}。请为所有基因输入有效数值")
    except Exception as e:
        return render_template('index.html',
                            gene_names=GENE_NAMES,
                            error=f"处理错误: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)