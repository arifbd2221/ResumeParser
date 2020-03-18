from django.shortcuts import render
from .models import Resume, Candidate
from django.core.files.storage import default_storage
import os
from pyresparser import ResumeParser

def home(request):

    top_candidates = dict()

    candidates = Candidate.objects.all()

    candidates = list(candidates)

    candidates.sort(key=lambda c: c.experience, reverse=True)
    
    return render(request, "app/home.html", {'candidates': candidates})



def handleResume(request):
    if request.method == 'POST':
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print('post')
        resume = request.FILES.get('resume', None)
        print(resume)
        if resume:
            saving=Resume(resume=resume)
            saving.save()
            media_path = os.path.join(BASE_DIR,'resumes')
            lpart = str(saving.resume).split('/')
            full_path=os.path.join(media_path,lpart[1])
            data = ResumeParser(str(full_path)).get_extracted_data()
            
            candidate = Candidate(name=data.get('name'),email=data.get('email'),
                                    phone=data.get('mobile_number'),experience=float(data.get('total_experience')),
                                    total_skills=len(data.get('skills')), designation=data.get('designation'),
                                    company= "N/A" if data.get('company_names') is None  else  data.get('company_names'))

            candidate.save()

            return render(request, "app/home.html", {})

    return render(request, "app/cvform.html", {})
