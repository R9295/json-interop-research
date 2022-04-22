MicroModal.init();

const parseData = (data, filter) => {
  let d = filter
    ? data.data.filter((item) => item.test.indexOf(filter) != -1)
    : data.data;
  const parsed = d.map((item) => {
    return {
      x: item.implementation,
      y: item.test,
      v: item.passed,
    };
  });
  parsed.sort((a, b) => a.y.localeCompare(b.y));
  return parsed;
};

const render = (filter = null) => {
  fetch("/analysis.json")
    .then((data) => {
      data.json().then((analysis) => {
        const parsedData = parseData(analysis, filter);
        const uniqueParsedLen = parsedData.length;
        console.log(parsedData, uniqueParsedLen);
        window.chart = new Chart("chart", {
          type: "matrix",
          data: {
            datasets: [
              {
                label: "My Matrix",
                data: parsedData,
                borderWidth: 1,
                borderColor(ctx) {
                  return Chart.helpers.color("white").rgbString();
                },
                backgroundColor(ctx) {
                  const value = ctx.dataset.data[ctx.dataIndex].v;
                  return Chart.helpers
                    .color(value ? "black" : "red")
                    .rgbString();
                },
                width(ctx) {
                  const a = ctx.chart.chartArea || {};
                  return (a.right - a.left) / 12 - 1;
                },
                height(ctx) {
                  return 100;
                },
              },
            ],
          },
          options: {
            maintainAspectRatio: false,
            onClick: (e, element) => {
              const index = element[0].index;
              const content = document.getElementById("modal-1-content");
              const title = document.getElementById("modal-1-title");
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
            legend: {
              display: false,
            },
            tooltips: {
              callbacks: {
                title() {
                  return "";
                },
                label(ctx) {
                  const v = ctx.dataset.data[ctx.dataIndex];
                  return ["x: " + v.x, "y: " + v.y, "v: " + v.v];
                },
              },
            },
            scales: {
              x: {
                type: "category",
                labels: [...new Set(parsedData.map((item) => item.x))],
                ticks: {
                  display: true,
                  color: "white",
                },
                gridLines: {
                  display: true,
                },
              },
              y: {
                type: "category",
                labels: [...new Set(parsedData.map((item) => item.y))],
                offset: true,
                reverse: false,
                ticks: {
                  display: true,
                  color: "white",
                },
                gridLines: {
                  display: true,
                },
              },
            },
          },
        });
      });
    })
    .catch(() => {
      document.getElementById("body").innerHTML =
        '<h1 style="color: #ffff">Cannot find file analysis.json in folder</h1>';
    });
};

const button = document.getElementById("button");
button.onclick = () => {
  if (window.chart) {
    window.chart.destroy();
  }
  filter = document.getElementById("filter").value;
  render(filter);
};
render();
