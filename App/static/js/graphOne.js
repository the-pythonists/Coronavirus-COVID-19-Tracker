function WorldCases() {
	fetch("http://127.0.0.1:8000/graphOne/")
        .then(response => response.json())
        .then(rsp => {
            countries = rsp["countries"]
            cases = rsp["cases"]
	new Chart(document.getElementById("bar-chart"), {
    type: 'bar',
    data: {
      labels: countries,
      datasets: [
        {
          label: "Total Cases in Countries",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#FF7F50","#008B8B","#006400","#2F4F4F","#ADFF2F"],
          data: cases

        }
      ]
    },
    options: {
      legend: { 
        display: true ,
        legendText: "2010",
        position: 'top',
      labels: {
                fontColor: "#000080",
            }
          },
      title: {
        display: true,
        text: 'Highest Cases in 10 countries'
      }
    }
});
	});
}
WorldCases()

function IndiaCases(){
  fetch("http://127.0.0.1:8000/graphTwo/")
        .then(response => response.json())
        .then(rsp => {
            states = rsp["states"]
            confirmed = rsp["confirmedCases"]
  new Chart(document.getElementById("line-chart"), {
  type: 'line',
  data: {
    labels: states,
    datasets: [{ 
        data: confirmed,
        label: "Cases",
        borderColor: "#3e95cd",
        fill: false
      }
    ]
  },
  options: {
    title: {
      display: true,
      text: 'India State Wise Cases'
    },
    scaleShowValues:true,
    scales:{
      xAxes:[{
        ticks:{
          autoSkip:false
        }
      }]
    }
  }
});
});
}
IndiaCases()

function ActiveCases(){
  fetch("http://127.0.0.1:8000/graphFour/")
        .then(response => response.json())
        .then(rsp => {
            states = rsp["states"]
            active = rsp["active"]
  new Chart(document.getElementById("line-chart3"), {
  type: 'line',
  data: {
    labels: states,
    datasets: [{ 
        data: active,
        label: "Active",
        borderColor: "#3e95cd",
        fill: false
      }
    ]
  },
  options: {
    title: {
      display: true,
      text: 'Active Cases'
    },
    scaleShowValues:true,
    scales:{
      xAxes:[{
        ticks:{
          autoSkip:false
        }
      }]
    }
  }
});
});
}
ActiveCases()

function RecoveredCases(){
  fetch("http://127.0.0.1:8000/graphThree/")
        .then(response => response.json())
        .then(rsp => {
            states = rsp["states"]
            recovered = rsp["recovered"]
  new Chart(document.getElementById("line-chart2"), {
  type: 'line',
  data: {
    labels: states,
    datasets: [{ 
        data: recovered,
        label: "Recovered",
        borderColor: "#3e95cd",
        fill: false
      }
    ]
  },
  options: {
    title: {
      display: true,
      text: 'Recovered Cases'
    },
    scaleShowValues:true,
    scales:{
      xAxes:[{
        ticks:{
          autoSkip:false
        }
      }]
    }
  }
});
});
}
RecoveredCases()

function DeathCases(){
  fetch("http://127.0.0.1:8000/graphFive/")
        .then(response => response.json())
        .then(rsp => {
            states = rsp["states"]
            dead = rsp["deaths"]
  new Chart(document.getElementById("line-chart4"), {
  type: 'line',
  data: {
    labels: states,
    datasets: [{ 
        data: dead,
        label: "Deaths",
        borderColor: "#3e95cd",
        fill: false
      }
    ]
  },
  options: {
    title: {
      display: true,
      text: 'Deaths Cases'
    },
    scaleShowValues:true,
    scales:{
      xAxes:[{
        ticks:{
          autoSkip:false
        }
      }]
    }
  }
});
});
}
DeathCases()