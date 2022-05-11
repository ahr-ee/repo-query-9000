import React from "react";
import { useSelector } from "react-redux"
import getVal from "../utility";
import SocketHandler from "../websocket/SocketHandler"


const Home = () => {
    const state = useSelector((state) => state)
    const socketHandler = new SocketHandler()

    const queryUsername = (username) => {
        socketHandler.queryUsernameRequest(username)
    }

    const QueryBox = () => {
        return <div>
            <input id='queryUsernameVal' type='text'/>
            <button id='submitTestIn' onClick={() => queryUsername(getVal('queryUsernameVal'))}>submit</button>
        </div>
    }

    const RepoView = () => {
        console.log(state)
        if (state.length > 0) {
            var username = Object.keys(state[0])[0]
            var name = Object.values(state[0])
            console.log(username)
            console.log(name)
        }
    }

    return <div><div>{QueryBox()}</div><div>{RepoView()}</div></div>
};

export default Home