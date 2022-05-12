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
        if (state.length > 0) {
            var username = Object.keys(state[0])[0]
            var repos = Object.values(state[0])[0]['repos']

            return <div>
                <h2>
                    {username}
                </h2>
                <div>
                    {
                        repos.map((el) => (
                            <div>
                                <h3>{el['name']}</h3>
                                <div>html_url: {el['html_url']}</div>
                                <div>description: {el['description']}</div>
                                <div>language: {el['language']}</div>
                            </div>
                        ))
                    }
                </div>
            </div>
        }
    }

    return <div><div>{QueryBox()}</div><div>{RepoView()}</div></div>
};

export default Home