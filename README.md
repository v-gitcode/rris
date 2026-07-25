# RRIS - Inter-School Cultural Festival 🎭

## About the Festival

**RRIS** (Ram Ratna International School) hosts an annual inter-school cultural, literary, academic, and performing arts festival. This festival brings together students from various schools to celebrate creativity, talent, and academic excellence.

An inter-school cultural, literary, academic and performing arts festival organized by Ram Ratna International School & Ram Ratna Prathama Pre-School.

### Organizing Institutions
- **Ram Ratna International School**
- **Ram Ratna Prathama Pre-School**

## Festival Categories

### 🎨 Cultural Events
- Classical Dance Performances
- Contemporary Dance
- Musical Performances
- Drama & Theatre
- Instrumental Music

### 📚 Literary Events
- Poetry Reading
- Story Telling
- Essay Writing
- Debate Competition
- Creative Writing

### 🏆 Academic Events
- Science Exhibitions
- Mathematics Competition
- General Knowledge Quiz
- Project Showcase
- Innovation Challenge

### 🎤 Performing Arts
- Choir Performances
- Solo Singing
- Band Performance
- Comic Acts
- Fashion Show

## Project Details

This repository contains:
- Festival management documentation
- Event schedules and timelines
- Participant information
- Results and achievements
- Media and content

## Technology Stack

- **Language:** Python
- **Automation:** GitHub Actions
- **AI Integration:** Google AI Studio (Gemini API)

## AI Integration

This project integrates with **Google AI Studio** to:
- Generate event descriptions automatically
- Create festival schedules
- Analyze feedback and responses
- Generate marketing content
- Assist in content creation

### Workflow
- **Trigger:** Push to main branch or Pull Requests
- **Script:** `scripts/ai_integration.py`
- **API:** Google Generative AI (Gemini)

## Getting Started

### Prerequisites
- Python 3.11+
- Google AI Studio API Key
- GitHub Account

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/v-gitcode/rris.git
   cd rris
   ```

2. **Install dependencies**
   ```bash
   pip install google-generativeai
   ```

3. **Add Google API Key**
   - Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Add it as a GitHub secret: `GOOGLE_API_KEY`

4. **Run AI Integration Script**
   ```bash
   python scripts/ai_integration.py
   ```

## File Structure

```
rris/
├── README.md                          # This file
├── .github/
│   └── workflows/
│       └── google-ai-integration.yml  # GitHub Actions workflow
├── scripts/
│   └── ai_integration.py              # AI integration script
└── docs/                              # Documentation (planned)
```

## Contributing

Contributions are welcome! Please feel free to:
- Report issues
- Suggest improvements
- Submit pull requests
- Add new features

## License

This project is open source and available under the MIT License.

## Contact

For more information about the RRIS Festival, contact:
- **School:** Ram Ratna International School
- **Email:** info@ramratna.edu
- **Repository Owner:** [v-gitcode](https://github.com/v-gitcode)

---

**Last Updated:** July 25, 2026
**Status:** 🚀 Active Development with AI Integration
