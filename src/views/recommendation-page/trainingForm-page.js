import { useState } from 'react';
import { Box, Button, Checkbox, FormControl, FormControlLabel, FormGroup, FormLabel, Grid, TextField, Typography, MenuItem } from '@mui/material';
import axios from 'axios';

const ingredientsList = [
    'Légumes frais (carottes, brocolis, épinards, etc.)',
    'Fruits frais (pommes, bananes, fraises, etc.)',
    'Viandes maigres (poulet, dinde, poisson, etc.)',
    'Produits laitiers (yaourt, fromage, lait, etc.)',
    'Céréales et grains (riz, pâtes, quinoa, etc.)',
    'Noix et graines (amandes, noix, graines de chia, etc.)',
    'Légumineuses (haricots, lentilles, pois chiches, etc.)',
    "Huiles et vinaigres (huile d'olive, vinaigre balsamique, etc.)",
    'Épices et assaisonnements (sel, poivre, origan, etc.)',
  ];
  
  const equipmentList = [
    'Haltères',
    'Kettlebells',
    'Barres de poids',
    'Banc de musculation',
    'Tapis de yoga',
    'Corde à sauter',
    'Ballon de stabilité',
    'Bande de résistance',
    'Machine elliptique',
    'Tapis de course',
    'Vélo stationnaire',
    'Step aérobique',
  ];
  

const TrainingForm = () => {
  const [trainingGoal, setTrainingGoal] = useState('');
  const [selectedIngredients, setSelectedIngredients] = useState([]);
  const [selectedEquipment, setSelectedEquipment] = useState([]);
  const [trainingFrequency, setTrainingFrequency] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Envoi des données au backend avec Axios
      const response = await axios.post('URL_ENDPOINT_PYTHON', {
        trainingGoal,
        selectedIngredients,
        selectedEquipment,
        trainingFrequency,
      });
      console.log('Réponse du serveur:', response.data);
      // Réinitialiser le formulaire après soumission réussie si nécessaire
      setTrainingGoal('');
      setSelectedIngredients([]);
      setSelectedEquipment([]);
      setTrainingFrequency('');
    } catch (error) {
      console.error('Erreur lors de la soumission du formulaire:', error);
    }
  };

  const handleIngredientChange = (event) => {
    const { value } = event.target;
    setSelectedIngredients(
      selectedIngredients.includes(value)
        ? selectedIngredients.filter((item) => item !== value)
        : [...selectedIngredients, value]
    );
  };

  const handleEquipmentChange = (event) => {
    const { value } = event.target;
    setSelectedEquipment(
      selectedEquipment.includes(value)
        ? selectedEquipment.filter((item) => item !== value)
        : [...selectedEquipment, value]
    );
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Choisissez vos préférences d'entraînement
      </Typography>
      <form onSubmit={handleSubmit}>
        <Grid container spacing={3}>
          <Grid item xs={12}>
            <FormControl component="fieldset">
              <FormLabel component="legend">Objectif d'entraînement</FormLabel>
              <TextField
                fullWidth
                select
                variant="outlined"
                value={trainingGoal}
                onChange={(e) => setTrainingGoal(e.target.value)}
              >
                <MenuItem value="Perte de poids">Perte de poids</MenuItem>
                <MenuItem value="Gain de masse musculaire">Gain de masse musculaire</MenuItem>
                <MenuItem value="Amélioration de l'endurance">Amélioration de l'endurance</MenuItem>
              </TextField>
            </FormControl>
          </Grid>
          <Grid item xs={12}>
            <FormControl component="fieldset">
              <FormLabel component="legend">Ingrédients disponibles dans votre réfrigérateur</FormLabel>
              <FormGroup>
                {ingredientsList.map((ingredient) => (
                  <FormControlLabel
                    key={ingredient}
                    control={<Checkbox checked={selectedIngredients.includes(ingredient)} onChange={handleIngredientChange} value={ingredient} />}
                    label={ingredient}
                  />
                ))}
              </FormGroup>
            </FormControl>
          </Grid>
          <Grid item xs={12}>
            <FormControl component="fieldset">
              <FormLabel component="legend">Matériaux disponibles</FormLabel>
              <FormGroup>
                {equipmentList.map((equipment) => (
                  <FormControlLabel
                    key={equipment}
                    control={<Checkbox checked={selectedEquipment.includes(equipment)} onChange={handleEquipmentChange} value={equipment} />}
                    label={equipment}
                  />
                ))}
              </FormGroup>
            </FormControl>
          </Grid>
          <Grid item xs={12}>
            <FormControl component="fieldset">
              <FormLabel component="legend">Nombre de séances d'entraînement par semaine</FormLabel>
              <TextField
                fullWidth
                select
                variant="outlined"
                value={trainingFrequency}
                onChange={(e) => setTrainingFrequency(e.target.value)}
              >
                <MenuItem value="1">1 fois par semaine</MenuItem>
                <MenuItem value="2">2 fois par semaine</MenuItem>
                <MenuItem value="3">3 fois par semaine</MenuItem>
                {/* Ajoutez plus d'options selon vos besoins */}
              </TextField>
            </FormControl>
          </Grid>
          <Grid item xs={12}>
            <Button type="submit" variant="contained" color="primary">
              Soumettre
            </Button>
          </Grid>
        </Grid>
      </form>
    </Box>
  );
};

export default TrainingForm;

