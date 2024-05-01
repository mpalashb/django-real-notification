const ws_url = `ws://${window.location.host}/ws/notify/`;
const socket = new WebSocket(ws_url);

socket.onmessage = (e) => {
  console.log(JSON.parse(e.data));
  const notifyEle = document.querySelector(".notification_count");
  if (notifyEle) {
    notifyEle.innerText = parseInt(JSON.parse(e.data).unread_count);
  }
};
