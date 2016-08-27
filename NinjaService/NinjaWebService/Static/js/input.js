
export class InputView extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      ws : new WebSocket("ws://" + location.host + "/input")
    };
    this.state.ws.onopen = function(event) {
        console.log("ws connected");
    };
    this.state.ws.onmessage = function(event) {
        var data = JSON.parse(event.data);
        // Todo
    };
  }
  componentDidMount() {
    window.addEventListener('keydown', this.handleKeyDown.bind(this));
  }
  componentWillUnmount() {
    window.removeEventListener('keydown', this.handleKeyDown.bind(this));
  }
  handleKeyDown(event) {
      event.preventDefault();
      ws.send(JSON.stringify({
          "key": event.keyCode
      }))
  }
  handleTouchStart(event) {

  }
  handleTouchEnd(event) {

  }
  render() {
    return (
      <div className='input_view'>
        xixixi
      </div>
    );
  }
};