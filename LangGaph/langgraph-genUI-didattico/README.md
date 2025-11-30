# 🎨 Generative UI con LangGraph

Un progetto didattico che dimostra come costruire **interfacce utente generative** usando Python (LangGraph) e React.

![Demo](https://img.shields.io/badge/Status-Educational-blue) ![Python](https://img.shields.io/badge/Python-3.12-green) ![React](https://img.shields.io/badge/React-19.2-blue) ![LangGraph](https://img.shields.io/badge/LangGraph-1.0-orange)

## 📖 Cos'è?

Questo progetto mostra come un agente AI può generare **componenti UI dinamici** invece di semplice testo. Quando chiedi informazioni sul meteo, invece di ricevere una risposta testuale, ottieni una card interattiva con icone colorate e dati strutturati.

### Demo

```
User: "What's the weather today?"

Invece di:
  "It's 22°C with 45% humidity and 12 km/h wind"

Ottieni:
  ┌─────────────────────────────────┐
  │ ☀️ Weather Forecast             │
  │ Current weather for New York   │
  │                                 │
  │ 🌡️ Temp    💧 Humidity  💨 Wind│
  │ 22°C       45%          12 km/h│
  └─────────────────────────────────┘
```

## 🎯 Obiettivo Didattico

Questo è un **esempio educativo semplificato** per capire:

- ✅ Come funziona **LangGraph** (grafi, state, nodi)
- ✅ L'integrazione tra **Python backend** e **React frontend**
- ✅ Il pattern **Generative UI** 
- ✅ Come la **LangGraph CLI** orchestra tutto

**Non è un'app production-ready** - usa dati mock e logica semplificata per focalizzarsi sui concetti fondamentali.

## 🏗️ Architettura

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   Browser   │─────▶│   Next.js    │─────▶│  LangGraph  │
│   (Client)  │◀─────│  (Frontend)  │◀─────│   Server    │
└─────────────┘      └──────────────┘      └─────────────┘
                                                   │
                                                   ▼
                                            ┌──────────────┐
                                            │Python Agent  │
                                            │+ React UI    │
                                            └──────────────┘
```

- **Backend**: Python con LangGraph per la logica dell'agente
- **UI Components**: React (TypeScript) con Tailwind CSS
- **Frontend**: Next.js per la chat interface
- **Bridge**: LangGraph CLI compila e serve tutto

## 🚀 Quick Start

### Prerequisiti

- Python 3.12+
- Node.js 20+
- OpenAI API Key

### Installazione

1. **Clone il repository**
   ```bash
   git clone https://github.com/agenti/langraph.git
   cd langraph
   ```

2. **Setup Python**
   ```fish
   python3 -m venv .venv
   source .venv/bin/activate.fish  # o activate su Bash/Zsh
   pip install -r requirements.txt
   ```

3. **Setup Node.js**
   ```bash
   npm install
   ```

4. **Configura le API Keys**
   ```bash
   cp .env.example .env
   # Modifica .env e aggiungi la tua OPENAI_API_KEY
   ```

### Esecuzione

**Terminale 1 - Backend (LangGraph)**
```fish
source .venv/bin/activate.fish
export OPENAI_API_KEY="sk-..."
langgraph dev
```

**Terminale 2 - Frontend (Next.js)**
```bash
npm run dev
```

Apri il browser su [`http://localhost:3000`](http://localhost:3000)

## 📁 Struttura del Progetto

```
.
├── src/
│   ├── agent.py              # 🐍 Agente LangGraph (Python)
│   ├── agente/
│   │   ├── ui.tsx           # ⚛️  Componenti React
│   │   └── styles.css       # 🎨 Stili Tailwind
│   └── app/
│       ├── page.tsx         # 💬 Interfaccia chat
│       ├── layout.tsx       # 📐 Layout globale
│       └── globals.css      # 🎨 Stili globali
├── langgraph.json           # ⚙️  Config LangGraph
├── package.json             # 📦 Dipendenze Node.js
├── requirements.txt         # 📦 Dipendenze Python
├── GUIDA.md                 # 📚 Guida dettagliata
└── README.md                # 👈 Questo file
```

## 📚 Documentazione

Per una **spiegazione completa e dettagliata** del progetto, leggi [`GUIDA.md`](./GUIDA.md) che copre:

- Architettura del sistema in dettaglio
- Come funziona LangGraph (grafi, state, nodi)
- Spiegazione di React e Next.js per backend developers
- Il flusso completo dei dati passo per passo
- Come funziona la LangGraph CLI
- FAQ e troubleshooting

## 🛠️ Tecnologie Utilizzate

### Backend
- **[LangGraph](https://github.com/langchain-ai/langgraph)** - Framework per agenti AI
- **[LangChain](https://github.com/langchain-ai/langchain)** - Orchestrazione LLM
- **[OpenAI](https://openai.com/)** - Modello GPT-4o-mini

### Frontend
- **[React](https://react.dev/)** - UI library
- **[Next.js](https://nextjs.org/)** - React framework
- **[TypeScript](https://www.typescriptlang.org/)** - Type safety
- **[Tailwind CSS](https://tailwindcss.com/)** - Styling
- **[Lucide Icons](https://lucide.dev/)** - Icone

### Tools
- **[LangGraph CLI](https://github.com/langchain-ai/langgraph-cli)** - Dev server e bundling

## 🎓 Per Chi è Questo Progetto?

Ideale per:
- 🐍 **Python developers** che vogliono capire React e frontend
- ⚛️  **Frontend developers** che vogliono capire LangGraph e AI agents
- 🤖 **AI enthusiasts** che vogliono costruire UI generative
- 📚 **Studenti** che vogliono un esempio pratico e ben documentato

## 🔄 Prossimi Passi

Dopo aver capito questo esempio, prova a:

1. **Aggiungere un nuovo componente UI** (es. HotelCard, ProductCard)
2. **Implementare LangChain tools** per chiamare API reali
3. **Aggiungere routing condizionale** (l'agent decide quale UI mostrare)
4. **Costruire un grafo multi-nodo** con logica più complessa

## 🤝 Contributing

Questo è un progetto educativo. Pull requests per migliorare la documentazione o gli esempi sono benvenute!

## 📄 Licenza

MIT License - vedi [LICENSE](LICENSE) per i dettagli

## 🙏 Credits

Basato sulla documentazione ufficiale di [LangGraph Generative UI](https://docs.langchain.com/langgraph-platform/generative-ui)

---

**⭐ Se questo progetto ti è stato utile, lascia una stella su GitHub!**

Per domande o feedback, apri una [Issue](https://github.com/agenti/langraph/issues) 💬
