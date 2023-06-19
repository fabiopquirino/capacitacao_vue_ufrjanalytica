<template>
    <v-simple-table>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">
              ID
            </th>
            <th class="text-left">
              Nome
            </th>
            <th class="text-left">
              Sobrenome
            </th>
            <th class="text-left">
              Idade
            </th>
            <th class="text-left">
              Gênero
            </th>
            <th class="text-left">
              Salário
            </th>
            <th class="text-left">
              Cidade
            </th>
            <th class="text-left">
              País
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="item in json_data_brasil"
            :key="item.id"
          >
            <td>{{ item.id }}</td>
            <td>{{ item.nome }}</td>
            <td>{{ item.sobrenome }}</td>
            <td>{{ item.idade }}</td>
            <td>{{ item.genero }}</td>
            <td>{{ item.salario }}</td>
            <td>{{ item.cidade }}</td>
            <td>{{ item.pais }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </template>

<script>
import json_data_brasil from "/assets/brasil.json"

export default {
    data () {
      return {
        json_data_brasil
      }
    },
  }
</script>