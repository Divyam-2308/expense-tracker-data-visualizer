import React, { useEffect } from 'react';
import { StatusBar } from 'expo-status-bar';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { NavigationContainer } from '@react-navigation/native';
import { View, Text, ActivityIndicator } from 'react-native';
import { useAuthStore } from './src/store/authStore';

// Temporary loading screen
function LoadingScreen() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: '#f8fafc' }}>
      <Text style={{ fontSize: 32, marginBottom: 20 }}>💰</Text>
      <Text style={{ fontSize: 24, fontWeight: 'bold', color: '#1e293b' }}>CashCraft</Text>
      <ActivityIndicator size="large" color="#22c55e" style={{ marginTop: 20 }} />
    </View>
  );
}

// Temporary home screen
function HomeScreen() {
  const { user, signOut } = useAuthStore();
  
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: '#f8fafc', padding: 20 }}>
      <Text style={{ fontSize: 32, marginBottom: 10 }}>💰 CashCraft</Text>
      <Text style={{ fontSize: 18, color: '#64748b', marginBottom: 20 }}>
        Welcome, {user?.email || 'Guest'}!
      </Text>
      <Text style={{ fontSize: 14, color: '#22c55e', textAlign: 'center' }}>
        ✅ Phase 1 Complete!{'\n'}
        App is connected to Supabase.
      </Text>
    </View>
  );
}

export default function App() {
  const { isLoading, initialize } = useAuthStore();

  useEffect(() => {
    initialize();
  }, []);

  if (isLoading) {
    return <LoadingScreen />;
  }

  return (
    <SafeAreaProvider>
      <NavigationContainer>
        <HomeScreen />
        <StatusBar style="auto" />
      </NavigationContainer>
    </SafeAreaProvider>
  );
}