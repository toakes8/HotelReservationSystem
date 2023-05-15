let saveFile = () => {
    // Get the data from each element on the form.
    const fName = document.getElementById("firstName");
    const lName = document.getElementById("lastName");
    const chIn = document.getElementById("checkin");
    const chOut = document.getElementById("checkout");
    const roomNum = document.getElementById("roomNumber")
    const crCard = document.getElementById("creditCard");

    // This variable stores all the data.
    let data = "\r First Name: " + fName.value + " \r\n " + "Last Name: " 
    + lName.value + " \r\n " + "Check-In Time: " + chIn.value + " \r\n " + "Check-Out Time: " 
    + chOut.value + " \r\n " + "Room Number: " + roomNum.value + "\r\n " + "Credit Card Information: " 
    + crCard.value;
    console.log(data); //printing form data into the console
    // Convert the text to BLOB.
    const textToBLOB = new Blob([data], { type: "text/plain" });
  
    function create_UUID(){
      var dt = new Date().getTime();
      var uuid = '4xxx-yxxx'.replace(/[xy]/g, function(c) {
      var r = (dt + Math.random()*16)%16 | 0;
      dt = Math.floor(dt/16);
      return (c=='x' ? r :(r&0x3|0x8)).toString(16);
      });
      return uuid;
      }

      console.log(create_UUID());
  
    let newLink = document.createElement("a");
    newLink.download = create_UUID()+".log";

    if (window.webkitURL != null) {
        newLink.href = window.webkitURL.createObjectURL(textToBLOB);
    } else {
        newLink.href = window.URL.createObjectURL(textToBLOB);
        newLink.style.display = "none";
        document.body.appendChild(newLink);
    }

    newLink.click();
};