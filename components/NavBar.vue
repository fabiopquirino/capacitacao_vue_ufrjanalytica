<template>
    <div>
      <v-app-bar
        color="deep-purple accent-4"
        dense
        dark
      >
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
  
        <v-toolbar-title><div>{{ $route.name }}</div></v-toolbar-title>
  
        <v-spacer></v-spacer>
  
        <v-btn icon>
          <v-icon>mdi-heart</v-icon>
        </v-btn>
  
        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
  
        <v-menu
          left
          bottom
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              icon
              v-bind="attrs"
              v-on="on"
            >
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </template>
  
          <v-list>
            <v-list-item><NuxtLink to="/">Home</NuxtLink></v-list-item>
            <v-list-item><NuxtLink to="/Brasil">Brasil</NuxtLink></v-list-item>
            <v-list-item><NuxtLink to="/Colombia">Colômbia</NuxtLink></v-list-item>
            <v-list-item><NuxtLink to="/Peru">Peru</NuxtLink></v-list-item>
          </v-list>
        </v-menu>
      </v-app-bar>
    </div>
  </template>