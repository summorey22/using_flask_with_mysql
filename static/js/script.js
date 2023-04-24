function loadData() {
    fetch('/data')
      .then(response => response.json())
      .then(data => {
        // Process data and display in container
        for (var i=0; i<data.length; i++) {
          console.log(data[i]);
        }
      });
}

loadData();