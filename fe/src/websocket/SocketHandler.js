import { store } from "../state/store"

export default class SocketHandler {
    constructor() {
        if (SocketHandler.instance) {
            return SocketHandler.instance
        }
        console.log("foo foo")
        this.socket = new WebSocket(
            'ws://127.0.0.1:8000/appserver'     
        )

        this.socket.onmessage = response => {
            this.handleResponse(response)
        }

        SocketHandler.instance = this
    }

    queryUsernameRequest(username) {
        this.sendRequest(username)
    }

    sendRequest(request) {
        this.socket.send(request)
    }

    handleResponse(response) {
        if(response){
            const responseData = JSON.parse(response.data)
            console.log(responseData)
            if(responseData === 'BAD REQUEST'){
                console.error("BAD REQUEST: Please try again.")
            }
            else{
                store.dispatch({type: "add", payload: responseData})
            }
        }
    }

}