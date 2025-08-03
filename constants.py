import streamlit as st  

skill_col_size = 5

def navigation():
    bar0, bar1, bar2, bar3, bar4= st.columns([0.1,1,1,1,1])
    bar1.page_link("app.py", label="Introduction", icon="🏠")
    bar2.page_link("pages/experience.py", label= "Experience", icon="📚")
    bar3.page_link("pages/portofolio.py", label="Portofolio", icon="🎨")
    bar4.page_link("pages/hackathons.py", label="Hackathons", icon="💻")
    st.write("")

# personal info
info = {
  'brief':
    """    
      Passionate Data Scientist with hands-on experience in data analysis, statistical modeling, machine learning, and deep learning. 
      Skilled in **Python**, **SQL**, and **Data visualization**, with a strong foundation in **Optical engineering**. 
      Proven track record in analytical projects, research, software migration, and AI-driven solutions. 
      Adept at developing and deploying ML models to extract actionable insights and drive innovation. 
      Seeking to leverage analytical expertise and engineering background to contribute to innovative AI and data-driven solutions.  Currently pursuing a Master’s degree at Aalto University.
    """,
  'name':'Ekaterina Ustiukhina', 
  'study':'Aalto University, MSc. in Data Science and Signal Processing',
  'study_msc':'Data Science and Signal Processing, [Aalto University](https://www.aalto.fi/en/study-options/signal-processing-and-data-science-computer-communication-and-information-sciences-master-of-science), 2024-2026',
  'study_bsc':'Laser and Optical Engineering, [ITMO University](https://en.itmo.ru/en/faculty/124/nauchno-obrazovatelnyy_centr_fotoniki_i_optoinformatiki.htm), 2016-2021',
  'location':'Helsinki, Finland',
  'interest':'Data Science | Data Analysis | Computer Optics',
  'skills': [
    '💻 Programming: Python, Matlab, Git',
    '📊 Data Analytics: SQL, Excel, Data Visualization',
    '👩‍🔬 Data Science & ML: Jupyter Notebook, Microsoft Azure ML Studio, Statistical Analysis, Linear Regression, Predictive Modeling',
    '🔬 Optics: Comsol, LabView, Zemax, SolidWorks, AutoCAD',
  ]
}

experience = [
  {
    "company": ":green[ElFys] | Optics Hardware Manufacturing",
    "role": "Project Engineer Intern",
    "date": "June 2023 - July 2023",
    "location": "Helsinki, Finland", 
    "content": 
      """
      - Conducted EQE and responsivity measurements for photodetector chip testing, integrating data processing for accuracy improvement.
      - Migrated legacy analysis software from Matlab to Python, utilizing Pandas, Numpy, and SciPy for data manipulation and linear regression, enhancing test efficiency and reducing computational time.
      """,
    "link": {
      "name": "Company Website",
      "url": "https://www.elfys.fi",
    }
  },
  {
    "company": ":blue[ITMO University]",
    "role": "Research Student",
    "date": "September 2020 - January 2022",
    "location": "St. Petersburg, Russia",
    "content": 
      """
      - Developed and modeled luminance meter tools to measure urban light distribution, contributing to environmental data research.
      - Authored several papers focusing on data modeling and analysis in luminance metering, with one project earning recognition at the Russian Congress of Young Scientists.
      - Applied statistical analysis and developed software for light measurement, reinforcing skills in data-driven environmental assessment.
      """,
    "link": {
      "name": "University Website",
      "url": "https://en.itmo.ru/en/faculty/124/nauchno-obrazovatelnyy_centr_fotoniki_i_optoinformatiki.htm"
    }
  }
]    

portfolio = [
  {
    'name': ':green[Bone Age Prediction] Using Deep Learning',
    'description': """
      Developed a deep learning pipeline to predict bone age from X-ray images, automating a key clinical assessment in pediatric endocrinology. 
      Evaluated and improved a baseline ResNet18 model by integrating advanced data augmentations and hyperparameter tuning, resulting in significantly lower mean absolute error and improved generalization. 
      The project included rigorous data preprocessing, validation, and statistical analysis to demonstrate measurable gains in prediction accuracy.
      - Python, Pandas, Scikit-Learn, Matplotlib, Jupyter Notebook.
      - Data Analysis, Preprocessing, Deep Learning Model Development, Model Evaluation.
      """,
    'files':[
      {
        'name': 'Project Report',
        'type': 'pdf',
        'zoom_level': 1.2,
        'path': 'src/Portfolio_Bone_Age_Prediction_report.pdf'
      },
      {
        'name': 'Jupyter Notebook',
        'type': 'ipynb',
        'path': 'src/Portfolio_Bone_Age_Prediction_notebook.pdf'
      }
    ],
  },
  {
    'name': ':blue[Predicting AIDS patient survival] in a drug study using Machine Learning',
    'description': """
      Contributed to a data science project focused on predicting survival outcomes for AIDS patients in the ACTG Study 175 dataset. 
      Prepared and preprocessed the clinical and demographic dataset by removing target-leaking columns, dropping duplicates and constants, encoding categorical variables, and standardizing continuous features to optimize them for modeling.
      Built and tuned the Random Forest classifier to predict patient survival. Applied class weighting to address class imbalance and used forward stepwise feature selection to identify key predictors, such as CD4 counts, Karnofsky scores, and prior antiretroviral therapy. 
      Evaluated the model using balanced accuracy, recall, precision, and F1 score, achieving a balanced accuracy near 65%—substantially above baseline.
      Project demonstrated the value of machine learning for healthcare prognostics and the importance of robust data preparation and feature selection.
      - Python, Pandas, Scikit-Learn, Matplotlib, Jupyter Notebook.
      - Data Analysis, Preprocessing, Feature Selection, Model Performance Evaluation.
      """,
    'files':[
      {
        'name': 'Project Report',
        'type': 'pdf',
        'zoom_level': 0.5,
        'path': 'src/Portfolio_Predicting_AIDS_Patient_Survival_report.pdf'
      },
    ],
  },
  {
    'name': ':green[Weather Effects] on Domestic Trips in Finland',
    'description': """
      Contributed to a group project analyzing how weather, specifically seasonal temperature changes, affects domestic leisure trips to key regions in Finland (Uusimaa, Southwest Finland, North Ostrobothnia, and Lapland). 
      Developed data processing and analysis pipeline in Python (using pandas, seaborn, matplotlib). 
      Handled cleaning, merging, and transforming large datasets (weather data from the Finnish Meteorological Institute and travel statistics from Statistics Finland), calculated seasonal averages, and performed statistical analysis to reveal trends and correlations. 
      Created the main visualizations (scatter plots, line, and bar charts) used in the report and presentation.
      The analysis demonstrated a clear positive correlation between warmer seasonal temperatures and increased domestic trips, with variations by region and season.
      - Python, pandas, seaborn, matplotlib, Jupyter Notebook.
      - Data Analysis, Preprocessing, Statistical Analysis, Data Visualization.
      """,
    'files':[
      {
        'name': 'Project Report',
        'type': 'pdf',
        'zoom_level': 1.2,
        'path': 'src/Portfolio_Weather_Effects_on_Domestic_Trips_in_Finland_report.pdf'
      }
    ],
  },
  {
    'name': ':orange[Design of custom prisms] in Zemax OpticStudio',
    'description': """
      Wrote Medium post on designing custom prisms in Zemax OpticStudio. 
      The post walks readers through the process of creating non-standard prism geometries for optical systems, including step-by-step instructions for defining custom surfaces, setting up material properties, and optimizing prism parameters for specific optical requirements.
      Demonstrated practical techniques for using Zemax's user-defined surface and CAD import features, and provided troubleshooting tips for common design challenges such as controlling beam deviation and minimizing aberrations.
      The article is aimed at optical engineers and students seeking to expand their skills in advanced optical design and simulation using Zemax OpticStudio.
      - Zemax OpticStudio, optical design, custom prism modeling, technical writing.
      """,
    'links':[
      {
        'name': 'Medium Post',
        'action': 'View',
        'link': 'https://medium.com/@loveska87/design-of-custom-prisms-in-zemax-opticstudio-ecc8b14e38dc'
      }
    ],
  },
]

hackathons = [
  {
    'name': ':orange[Aalto AI Hackathon] 🏆',
    'challenge': 'Entity and Concept Disambiguation in LLMs',
    "date": "June 2025",
    "location": "Espoo, Finland", 
    "content": 
      """
      Contributed to building an AI-powered pipeline that transforms VTT's fragmented innovation data into a clean, canonical knowledge graph using FAISS for semantic search, GPT-4.1-mini for disambiguation, and smart graph curation. 
      Augmented an LLM-chat with the data retrieval from a high-quality knowledge graph.
      Won the challenge with the team. 🏆
      - OpenAI API, Semantic Search, GPT-4.1, Streamlit
      """,
    "link": "https://www.aalto.fi/en/events/aaltoai-hackathon",
    "images": [
      {
        "path": "src/images/hackathon_aalto_ai_1.jpg",
        "width": 2
      },
      {
        "path": "src/images/hackathon_aalto_ai_2.jpeg",
        "width": 1
      }
    ]
  },
  {
    'name': ':blue[Junction]',
    'challenge': 'Sustainable Space Data',
    "date": "November 2024",
    "location": "Helsinki, Finland", 
    "content": 
      """
      Focused on using Copernicus Sentinel satellite imagery to assess dengue fever risk in Italy by identifying environmental conditions favorable to tropical mosquito breeding (e.g., temperature, humidity, standing water). 
      Developed a prototype early-warning system leveraging geospatial data; identified large water reservoirs, though fine-scale detection remained a technical stretch. 
      Gained hands-on experience in geospatial analysis, open-source tools, and public health applications of satellite data.
      - Copernicus Sentinels, Geospatial Data
      """,
    "link": "https://eu.junctionplatform.com/projects/junction-2024",
    "images": [
      {
        "path": "src/images/hackathon_junction_1.jpeg",
        "width": 1
      },
      {
        "path": "src/images/hackathon_junction_2.jpeg",
        "width": 2
      }
    ]
  },
  {
    'name': ':green[Hanken Quantum Hackathon] | Ultrahack',
    'challenge': 'Quantum computing in sustainable finance',
    "date": "November 2023",
    "location": "Helsinki, Finland", 
    "content": 
      """
      Leveraged quantum computing to drive innovation in sustainable finance.
      Collaborated with teammates to translate our quantum finance concept into a clear, user-friendly web/mobile interface using Figma. 
      Designed interactive mockups that demonstrated the core user journeys, enabling effective pitching and feedback.
      Worked closely with team members from technical and business backgrounds to ensure design aligned with the challenge’s requirements—visualizing how quantum computing can empower ESG reporting and financial data analysis.
      This experience improved my rapid prototyping skills, stakeholder communication, and ability to convey complex technology to diverse audiences through visual design—key for hackathon settings where clarity and speed are critical.
      - Figma, Quantum Computing, Sustainable Finance Innovations, ESG Reporting
      """,
    "link": "https://new.ultrahack.org/hackathons/hanken-quantum-hackathon-2023",
    "images": [
      {
        "path": "src/images/hackathon_ultrahack_1.jpeg",
        "width": 1
      }
    ]
  }
]

# Contacts 
linkedin_link = "www.linkedin.com/in/ekaterina-ustiukhina-867205257"