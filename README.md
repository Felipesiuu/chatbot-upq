# Chatbot UPQ: recuperación de información oficial con aprendizaje supervisado

Sistema de clasificación de texto que responde preguntas frecuentes sobre la
Universidad Politécnica de Querétaro (UPQ). Usa TF-IDF y modelos de aprendizaje
supervisado de scikit-learn, y se ejecuta 100 % de forma local (sin APIs ni
servicios externos).

**Materia:** Fundamentos de Inteligencia Artificial
**Institución:** Universidad Politécnica de Querétaro

**Integrantes:**
- López Soto Regina
- Munguía Guerrero Felipe de Jesús
- Zea Machuca Rogelio Iván

---

## Estructura del repositorio

```
chatbot-upq/
├── data/
│   └── corpus_upq.csv          # Corpus: texto, intencion, respuesta
├── notebooks/
│   └── entrenamiento.ipynb     # Carga, limpieza, TF-IDF y comparativa de modelos
├── models/
│   ├── modelo.pkl              # Modelo final entrenado
│   └── vectorizador.pkl        # Vectorizador TF-IDF entrenado
├── src/
│   └── utils.py                # Función de limpieza de texto compartida
├── app.py                      # Interfaz de chat en Streamlit
├── requirements.txt            # Dependencias del proyecto
└── README.md
```

---

## Instalación

**1. Clonar el repositorio**
```bash
git clone https://github.com/USUARIO/chatbot-upq.git
cd chatbot-upq
```

**2. Crear y activar el entorno virtual**
```bash
python -m venv venv
```
- Windows (PowerShell): `venv\Scripts\activate`
- Linux / macOS: `source venv/bin/activate`

**3. Instalar dependencias**
```bash
pip install -r requirements.txt
```

---

## Uso

### 1. Entrenar el modelo
```bash
jupyter notebook notebooks/entrenamiento.ipynb
```
Ejecutar todas las celdas en orden. Al terminar se generan
`models/modelo.pkl` y `models/vectorizador.pkl`.

### 2. Levantar la interfaz de chat
```bash
streamlit run app.py
```
La aplicación se abre en `http://localhost:8501`.

---

## Corpus de datos

| Intención | Descripción | Nº de variantes |
|-----------|-------------|-----------------|
| _pendiente_ | | |

---

## Resultados

| Modelo | Accuracy | Precision (macro) | Recall (macro) | F1-score (macro) |
|--------|----------|-------------------|----------------|------------------|
| _pendiente_ | | | | |

**Modelo seleccionado:** _pendiente, con su justificación._

---

## Manejo de casos no reconocidos (fallback)

Si la confianza de la predicción es menor al umbral definido (`UMBRAL = pendiente`),
el chatbot responde con un mensaje genérico en lugar de dar una respuesta
incorrecta.

---

## Tecnologías

Python 3.11 · pandas · NumPy · scikit-learn · joblib · Matplotlib · Seaborn · Streamlit · Jupyter