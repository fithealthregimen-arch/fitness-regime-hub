---
layout: post
title: "4-Site Skinfold Body Fat Calculator (Durnin & Womersley)"
description: "Interactive calculator using the 4-site skinfold method with age-specific equations to estimate body fat percentage."
categories: [Calculators]
tags: [body fat, calculator, skinfold, durnin-womersley]
date: 2025-01-20 12:00:00 +0000
image: /assets/images/default-post.jpg
---

<style>
/* Namespaced styles for the calculator to avoid conflicts */
.skinfold-calculator-wrapper * { margin: 0 !important; padding: 0 !important; box-sizing: border-box !important; font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, sans-serif !important; }
.skinfold-calculator-wrapper { --primary-green:#047857 !important; --secondary-green:#059669 !important; --accent-green:#10B981 !important; --light-green:#D1FAE5 !important; --bg-gradient:linear-gradient(135deg,#F0FDF4,#ECFDF5) !important; --text-primary:#0F172A !important; --text-secondary:#334155 !important; --text-muted:#64748B !important; --border-color:#A7F3D0 !important; --card-bg:#FFFFFF !important; background:var(--bg-gradient) !important; color:var(--text-primary) !important; line-height:1.5 !important; padding:15px !important; border-radius: 16px !important; }
.skinfold-main-container { max-width: 1000px !important; margin: 0 auto !important; background: var(--card-bg) !important; border-radius: 20px !important; box-shadow: 0 25px 50px -12px rgba(4,120,87,.15) !important; border: 1px solid var(--border-color) !important; overflow: hidden !important; position: relative !important; }
.skinfold-header-section { text-align: center !important; padding: 25px 20px !important; background: linear-gradient(135deg,var(--primary-green),var(--secondary-green)) !important; color: #fff !important; }
.skinfold-main-title { font-size: 32px !important; font-weight: 800 !important; margin-bottom: 8px !important; }
.skinfold-subtitle { font-size: 16px !important; opacity: .9 !important; max-width: 600px !important; margin: 0 auto !important; }
.skinfold-info-box { background: var(--light-green) !important; border: 2px solid var(--accent-green) !important; border-radius: 12px !important; padding: 16px 20px !important; margin: 20px 0 !important; font-size: 14px !important; font-weight: 600 !important; color: var(--primary-green) !important; display: flex !important; align-items: center !important; gap: 10px !important; }
.skinfold-calculator-form { padding: 25px 20px !important; background: var(--card-bg) !important; }
.skinfold-form-grid { display: grid !important; grid-template-columns: repeat(auto-fit,minmax(280px,1fr)) !important; gap: 18px !important; margin-bottom: 20px !important; }
.skinfold-input-group { background: linear-gradient(145deg,#FFFFFF,#F8FAFC) !important; padding: 18px !important; border-radius: 12px !important; border: 2px solid var(--border-color) !important; transition: all .3s cubic-bezier(.4,0,.2,1) !important; position: relative !important; }
.skinfold-input-label { display: flex !important; align-items: center !important; gap: 10px !important; font-weight: 700 !important; color: var(--text-primary) !important; font-size: 16px !important; margin-bottom: 12px !important; }
.skinfold-input-icon { font-size: 20px !important; padding: 8px !important; background: linear-gradient(135deg,var(--primary-green),var(--secondary-green)) !important; border-radius: 10px !important; color: #fff !important; min-width: 36px !important; text-align: center !important; }
.skinfold-input-field, .skinfold-select-field { width: 100% !important; padding: 16px 20px !important; font-size: 16px !important; font-weight: 500 !important; border: 2px solid var(--border-color) !important; border-radius: 12px !important; background: var(--card-bg) !important; color: var(--text-primary) !important; transition: all .3s ease !important; outline: none !important; }
.skinfold-unit-toggle { display:flex !important; background: var(--light-green) !important; border-radius:12px !important; padding:4px !important; margin-top:12px !important; border:1px solid var(--border-color) !important; }
.skinfold-unit-btn { flex:1 !important; padding:12px 16px !important; border:none !important; background:transparent !important; color:var(--text-secondary) !important; font-weight:600 !important; font-size:14px !important; border-radius:8px !important; cursor:pointer !important; transition: all .3s ease !important; }
.skinfold-unit-btn.active { background: linear-gradient(135deg,var(--primary-green),var(--secondary-green)) !important; color:#fff !important; box-shadow: 0 4px 12px rgba(4,120,87,.3) !important; }
.skinfold-measurements-grid { display: grid !important; grid-template-columns: repeat(auto-fit,minmax(250px,1fr)) !important; gap: 18px !important; margin: 20px 0 !important; }
.skinfold-calculate-btn { width: 100% !important; padding: 20px 40px !important; background: linear-gradient(135deg,var(--primary-green),var(--secondary-green)) !important; color:#fff !important; border:none !important; border-radius:16px !important; font-size:18px !important; font-weight:700 !important; cursor:pointer !important; transition: all .3s ease !important; display:flex !important; align-items:center !important; justify-content:center !important; gap: 12px !important; box-shadow: 0 8px 25px rgba(4,120,87,.3) !important; }
.skinfold-results-container { margin-top: 30px !important; opacity: 0 !important; transform: translateY(20px) !important; transition: all .5s ease !important; max-height: 0 !important; overflow: hidden !important; }
.skinfold-results-container.show { opacity: 1 !important; transform: translateY(0) !important; max-height: 5000px !important; }
.skinfold-results-header { background: linear-gradient(135deg,var(--primary-green),var(--secondary-green)) !important; color:#fff !important; padding:25px 30px !important; border-radius: 16px 16px 0 0 !important; text-align:center !important; }
.skinfold-results-title { font-size: 24px !important; font-weight: 700 !important; display:flex !important; align-items:center !important; justify-content:center !important; gap: 12px !important; }
.skinfold-main-results { display:grid !important; grid-template-columns:1fr 1fr !important; background: linear-gradient(145deg,#F8FAFC,var(--card-bg)) !important; border-bottom: 1px solid var(--border-color) !important; }
.skinfold-result-item { padding: 30px !important; text-align:center !important; border-right:1px solid var(--border-color) !important; }
.skinfold-result-item:last-child { border-right:none !important; }
.skinfold-result-number { font-size:42px !important; font-weight: 800 !important; background: linear-gradient(135deg,var(--primary-green),var(--secondary-green)) !important; -webkit-background-clip:text !important; -webkit-text-fill-color:transparent !important; background-clip:text !important; margin-bottom: 8px !important; display:block !important; }
.skinfold-result-label { color: var(--text-secondary) !important; font-size: 16px !important; font-weight: 600 !important; text-transform: uppercase !important; letter-spacing: .5px !important; }
@media (max-width:768px){ .skinfold-main-results{ grid-template-columns:1fr !important;} }
</style>

<div class="skinfold-calculator-wrapper">
  <div class="skinfold-main-container">
    <div class="skinfold-header-section">
      <h1 class="skinfold-main-title">4-Site Skinfold Body Fat Calculator</h1>
      <p class="skinfold-subtitle">Measure your body fat percentage using the Durnin & Womersley method</p>
    </div>

    <div class="skinfold-calculator-form">
      <div class="skinfold-info-box">ℹ️ <strong>Simple & Accurate:</strong> Enter your age, gender, and four skinfold measurements to get your estimated body fat percentage.</div>

      <form id="skinfoldCalculatorForm">
        <div class="skinfold-form-grid">
          <div class="skinfold-input-group">
            <label class="skinfold-input-label"><span class="skinfold-input-icon">👤</span>Gender</label>
            <select id="genderSelect" class="skinfold-select-field" required>
              <option value="">Select Your Gender</option>
              <option value="male">Male</option>
              <option value="female">Female</option>
            </select>
          </div>
          <div class="skinfold-input-group">
            <label class="skinfold-input-label"><span class="skinfold-input-icon">🎂</span>Age</label>
            <input type="number" id="ageInput" class="skinfold-input-field" placeholder="Enter your age" min="16" max="72" step="1" required>
          </div>
        </div>

        <div class="skinfold-input-group">
          <label class="skinfold-input-label"><span class="skinfold-input-icon">📏</span>Measurement Units</label>
          <div class="skinfold-unit-toggle">
            <button type="button" id="mmButton" class="skinfold-unit-btn active">Millimeters (mm)</button>
            <button type="button" id="inchButton" class="skinfold-unit-btn">Inches</button>
          </div>
        </div>

        <h3 style="color: var(--primary-green) !important; font-size: 20px !important; margin: 25px 0 15px 0 !important; text-align: center !important;">📐 Take Your 4 Skinfold Measurements</h3>

        <div class="skinfold-measurements-grid">
          <div class="skinfold-input-group"><label class="skinfold-input-label"><span class="skinfold-input-icon">💪</span>Biceps</label><input type="number" id="bicepsInput" class="skinfold-input-field" placeholder="Enter measurement" step="0.1" min="1" max="50" required></div>
          <div class="skinfold-input-group"><label class="skinfold-input-label"><span class="skinfold-input-icon">🔧</span>Triceps</label><input type="number" id="tricepsInput" class="skinfold-input-field" placeholder="Enter measurement" step="0.1" min="1" max="50" required></div>
          <div class="skinfold-input-group"><label class="skinfold-input-label"><span class="skinfold-input-icon">🎯</span>Subscapular</label><input type="number" id="subscapularInput" class="skinfold-input-field" placeholder="Enter measurement" step="0.1" min="1" max="50" required></div>
          <div class="skinfold-input-group"><label class="skinfold-input-label"><span class="skinfold-input-icon">⚡</span>Suprailiac</label><input type="number" id="suprailiacInput" class="skinfold-input-field" placeholder="Enter measurement" step="0.1" min="1" max="50" required></div>
        </div>

        <button type="submit" class="skinfold-calculate-btn">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="10"/></svg>
          Calculate My Body Fat Percentage
        </button>
      </form>

      <div id="resultsContainer" class="skinfold-results-container"></div>
    </div>
  </div>
</div>

<script>
(function(){
  const form=document.getElementById('skinfoldCalculatorForm');
  const genderSelect=document.getElementById('genderSelect');
  const ageInput=document.getElementById('ageInput');
  const bicepsInput=document.getElementById('bicepsInput');
  const tricepsInput=document.getElementById('tricepsInput');
  const subscapularInput=document.getElementById('subscapularInput');
  const suprailiacInput=document.getElementById('suprailiacInput');
  const resultsContainer=document.getElementById('resultsContainer');
  const mmButton=document.getElementById('mmButton');
  const inchButton=document.getElementById('inchButton');
  let isMM=true;
  mmButton.addEventListener('click',()=>toggleUnit(true));
  inchButton.addEventListener('click',()=>toggleUnit(false));
  form.addEventListener('submit',handleFormSubmit);

  function toggleUnit(useMM){ if(useMM===isMM) return; isMM=useMM; const inputs=[bicepsInput,tricepsInput,subscapularInput,suprailiacInput]; if(isMM){mmButton.classList.add('active');inchButton.classList.remove('active');inputs.forEach(i=>{ if(i.value){ i.value=(parseFloat(i.value)*25.4).toFixed(1);} i.placeholder='Enter in mm';});} else {inchButton.classList.add('active');mmButton.classList.remove('active');inputs.forEach(i=>{ if(i.value){ i.value=(parseFloat(i.value)/25.4).toFixed(2);} i.placeholder='Enter in inches';});} }

  function calculateBodyFat(age,gender,measurements,isMMInput){
    const measurementsMM=isMMInput?measurements:measurements.map(m=>m*25.4);
    const sum=measurementsMM.reduce((a,b)=>a+b,0);
    let bodyDensity;
    if(gender==='male'){
      if(age>=16&&age<=19){ bodyDensity=1.1620-(0.0630*Math.log10(sum)); }
      else if(age<=29){ bodyDensity=1.1631-(0.0632*Math.log10(sum)); }
      else if(age<=39){ bodyDensity=1.1422-(0.0544*Math.log10(sum)); }
      else if(age<=49){ bodyDensity=1.1620-(0.0700*Math.log10(sum)); }
      else { bodyDensity=1.1715-(0.0779*Math.log10(sum)); }
    } else {
      if(age>=16&&age<=19){ bodyDensity=1.1549-(0.0678*Math.log10(sum)); }
      else if(age<=29){ bodyDensity=1.1599-(0.0717*Math.log10(sum)); }
      else if(age<=39){ bodyDensity=1.1423-(0.0632*Math.log10(sum)); }
      else if(age<=49){ bodyDensity=1.1333-(0.0612*Math.log10(sum)); }
      else { bodyDensity=1.1339-(0.0645*Math.log10(sum)); }
    }
    const bodyFatPercent=((4.95/bodyDensity)-4.50)*100; return Math.max(bodyFatPercent,3);
  }

  function getBodyFatCategory(bodyFat,age,gender){
    let categories; if(gender==='male'){ if(age<30){categories={essential:3, athlete:6, fitness:14, average:18, obese:25};} else if(age<50){categories={essential:3, athlete:7, fitness:17, average:21, obese:28};} else {categories={essential:3, athlete:9, fitness:19, average:24, obese:30};} } else { if(age<30){categories={essential:10, athlete:14, fitness:21, average:25, obese:32};} else if(age<50){categories={essential:10, athlete:16, fitness:24, average:28, obese:35};} else {categories={essential:10, athlete:18, fitness:27, average:31, obese:38};} }
    if(bodyFat<=categories.essential) return {level:'Essential Fat', color:'#3B82F6', description:'Essential fat levels - minimum needed for health'};
    if(bodyFat<=categories.athlete) return {level:'Athletes', color:'#059669', description:'Athletic body fat levels'};
    if(bodyFat<=categories.fitness) return {level:'Fitness', color:'#10B981', description:'Fitness enthusiast levels'};
    if(bodyFat<=categories.average) return {level:'Average', color:'#F59E0B', description:'Average range for your age group'};
    if(bodyFat<=categories.obese) return {level:'Above Average', color:'#EF4444', description:'Above average body fat'};
    return {level:'Obese', color:'#DC2626', description:'Obesity range - health risks may be elevated'};
  }

  function handleFormSubmit(e){
    e.preventDefault();
    const gender=genderSelect.value; const age=parseInt(ageInput.value); const biceps=parseFloat(bicepsInput.value); const triceps=parseFloat(tricepsInput.value); const subscapular=parseFloat(subscapularInput.value); const suprailiac=parseFloat(suprailiacInput.value);
    if(!gender){ alert('Please select your gender'); return; }
    if(!age||age<16||age>72){ alert('Please enter a valid age between 16-72 years'); return; }
    if(!biceps||!triceps||!subscapular||!suprailiac){ alert('Please enter all four skinfold measurements'); return; }
    const measurements=[biceps,triceps,subscapular,suprailiac];
    const bodyFat=calculateBodyFat(age,gender,measurements,isMM);
    const category=getBodyFatCategory(bodyFat,age,gender);
    const sum=measurements.reduce((a,b)=>a+b,0); const sumMM=isMM?sum:sum*25.4;
    displayResults(bodyFat,category,sumMM,{gender,age,measurements,unit:isMM?'mm':'inches'});
  }

  function displayResults(bodyFat,category,sumMM,userData){
    const html=`
      <div class="skinfold-results-header"><div class="skinfold-results-title">Your Body Fat Results</div></div>
      <div class="skinfold-main-results">
        <div class="skinfold-result-item"><span class="skinfold-result-number">${bodyFat.toFixed(1)}%</span><div class="skinfold-result-label">Body Fat Percentage</div></div>
        <div class="skinfold-result-item"><span class="skinfold-result-number" style="color:${category.color} !important;">${category.level}</span><div class="skinfold-result-label">Fitness Category</div></div>
      </div>
      <div style="background:#fff;padding:20px 30px;border-bottom:1px solid var(--border-color) !important;">
        <div style="display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;">
          <div><strong>Age:</strong> ${userData.age}</div>
          <div><strong>Gender:</strong> ${userData.gender}</div>
          <div><strong>Sum of Skinfolds:</strong> ${sumMM.toFixed(1)} mm</div>
        </div>
      </div>`;
    resultsContainer.innerHTML=html;
    resultsContainer.classList.add('show');
    resultsContainer.scrollIntoView({behavior:'smooth',block:'start'});
  }
})();
</script>


