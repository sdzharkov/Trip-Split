import React from 'react';
import ReactDOM from 'react-dom';

class Hello extends React.Component {
  render() {
    return (
    <Card shadow={0} style={{width: '256px', height: '256px', background: '#3E4EB8'}}>
    <CardTitle expand style={{alignItems: 'flex-start', color: '#fff'}}>
        <h4 style={{marginTop: '0'}}>
            Featured event:<br />
            May 24, 2016<br />
            7-11pm
        </h4>
    </CardTitle>
    <CardActions border style={{borderColor: 'rgba(255, 255, 255, 0.2)', display: 'flex', boxSizing: 'border-box', alignItems: 'center', color: '#fff'}}>
        <Button colored style={{color: '#fff'}}>Add to Calendar</Button>
        <div className="mdl-layout-spacer"></div>
        <Icon name="event" />
    </CardActions>
  </Card>
    );
  }
}

ReactDOM.render(<Hello/>, document.getElementById('mdl-grid'));
