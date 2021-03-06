import { StatusBar } from 'expo-status-bar';
import React, { Component } from 'react';
import { StyleSheet, Text, Image, View } from 'react-native';

export default class App extends Component {
  constructor(){
    super()
    this.state={weather:""}
  }
  getweather=()=>{
    var url= ("https://fcc-weather-api.glitch.me/api/current?lat=35&lon=139")
    return fetch(url)
    .then(response=>response.json())
    .then(responsejson=>{
      this.setState({weather:responsejson})
    })
    .catch(error=>{console.error(error)})
  }
  componentDidMount=()=>{
    this.getweather()
  }
  render(){
    if(this.state.weather===""){
      return (
        <View style={styles.container}>
          <Text>Loading...</Text>
          <StatusBar style="auto" />
        </View>
      );
    }
    else{
      return (
        <View style={styles.container}>
          <View style={styles.subContainer}>
        <Text style={styles.title}>
          Weather Forecast
        </Text>
        <Image style={styles.cloudImage} source={require("./weather.png")}>
        </Image>
        <View style={styles.textContainer}>
          <Text style= {{fontSize:18}}>
            {this.state.weather.main.temp} degrees Centigrade
          </Text>
          <Text style= {{fontSize:20, margin:10}}>
            Humidity:{this.state.weather.main.humidity}
          </Text>
          <Text style= {{fontSize:20}}>
            {this.state.weather.weather[0].description}
          </Text>
        </View>
          </View>
        </View>
      );
    }
  
}
}

const styles = StyleSheet.create({
  container: {
   flex:1
  },
  subContainer : { 
    flex: 1, 
    borderWidth: 1, 
    alignItems: 'center' 
    },
    title:{ 
      marginTop: 50, 
      fontSize: 30,
      fontWeight: '550' 
    },
    cloudImage :{ 
      width: 200, 
      height: 200, 
      marginTop: 30 
    },
    textContainer : { 
      flex: 1,
      alignItems: 'center', 
      flexDirection:'row', 
      marginTop:-150
    }
});