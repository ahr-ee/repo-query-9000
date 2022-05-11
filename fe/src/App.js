import "./App.css"
import Header from './components/Header'
import React from "react"
import { BrowserRouter, Route, Switch} from 'react-router-dom'
import Home from './pages/Home'
import About from './pages/About'
import NotFound from "./pages/NotFound"

function App() {
    return (
        <BrowserRouter>
            <div className="App">
                <Header />

                <Switch>
                    <Route path='/' component={Home} exact/>
                    <Route path='/about' component={About} />
                    <Route component={NotFound} />
                </Switch>
            </div>
        </BrowserRouter>
    )
}

export default App;