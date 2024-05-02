const ws_url = `ws://${window.location.host}/ws/notify/`;
const socket = new WebSocket(ws_url);

socket.onmessage = (e) => {
  const messageData = JSON.parse(e.data);
  const username = messageData.user_to.username;
  const userID = messageData.user_to.userID;
  const unreadCount = messageData.unread_count;

  console.log(username, userID, unreadCount);

  const notifyEle = document.querySelector(".notification_count");
  if (notifyEle) {
    notifyEle.innerText = parseInt(unreadCount);
  }
};

// const ws_url = `ws://${window.location.host}/ws/notify/`;
// const socket = new WebSocket(ws_url);

// socket.onmessage = (e) => {
//   console.log(JSON.parse(e.data));
//   const notifyEle = document.querySelector(".notification_count");
//   if (notifyEle) {
//     notifyEle.innerText = parseInt(JSON.parse(e.data).unread_count);
//   }
// };
