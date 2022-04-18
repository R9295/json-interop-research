MicroModal.init();

const parseData = (data) => {
  return Object.keys(data).map((item) => {
    const name = item.split("vs");
    return {
      x: name[0],
      y: name[1],
      v: data[item].length,
    };
  });
};
fetch("/analysis.json")
  .then((data) => {
    data.json().then((analysis) => {
      const parsedData = parseData(analysis);
      const parsedLen = parsedData.length;
      const uniqueParsedLen = [...new Set(parsedData.map((item) => item.x))]
        .length;
      new Chart("chart", {
        type: "matrix",
        data: {
          datasets: [
            {
              label: "My Matrix",
              data: parsedData,
              backgroundColor(context) {
                const value = context.dataset.data[context.dataIndex].v;
                const alpha = value / 120;
                return Chart.helpers.color("red").alpha(alpha).rgbString();
              },
              width(context) {
                const a = context.chart.chartArea;
                if (!a) {
                  return 0;
                }
                return (
                  (a.right - a.left) / uniqueParsedLen - (uniqueParsedLen - 1)
                );
              },
              height(context) {
                const a = context.chart.chartArea;
                if (!a) {
                  return 0;
                }
                return (
                  (a.bottom - a.top) / uniqueParsedLen - (uniqueParsedLen - 1)
                );
              },
            },
          ],
        },
        options: {
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
              label(context) {
                const v = context.dataset.data[context.dataIndex];
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
              },
              gridLines: {
                display: false,
              },
            },
            y: {
              type: "category",
              labels: [...new Set(parsedData.map((item) => item.y))],
              offset: true,
              reverse: false,
              ticks: {
                display: true,
              },
              gridLines: {
                display: false,
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
