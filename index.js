MicroModal.init();

fetch("/analysis.json")
  .then((data) => {
    data.json().then((analysis) => {
      var data = {
        labels: Object.keys(analysis),
        datasets: [
          {
            label: "Dataset #1",
            backgroundColor: "#87AF5F",
            borderWidth: 2,
            hoverBackgroundColor: "#8197BF",
            hoverBorderColor: "#8197BF",
            data: Object.values(analysis).map((item) => item.length),
          },
        ],
      };
      var options = {
        maintainAspectRatio: false,
        scales: {
          y: {
            stacked: true,
            grid: {
              display: true,
              color: "#A293CB",
            },
          },
          x: {
            grid: {
              display: false,
            },
          },
        },
      };
      new Chart("chart", {
        type: "bar",
        options: {
          ...options,
          onClick: (e, element) => {
            var index = element[0].index;
            var content = document.getElementById("modal-1-content");
            var title = document.getElementById("modal-1-title");
            title.innerHTML = `<h3>${Object.keys(analysis)[index]}</h3>`;
            content.innerHTML = `<h5>Total entries: ${
              Object.values(analysis)[index].length
            }</h5><pre>${JSON.stringify(
              Object.values(analysis)[index],
              null,
              "\t"
            )}</pre>`;
            MicroModal.show("modal-1");
          },
        },
        data: data,
      });
    });
  })
  .catch(() => {
    document.getElementById("body").innerHTML =
      '<h1 style="color: #ffff">Cannot find file analysis.json in folder</h1>';
  });
