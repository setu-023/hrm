from rest_framework import serializers

from account.models import Account

class AccountSerializer(serializers.ModelSerializer):

	
		class Meta:
			model = Account
			fields ='__all__'
			extra_kwargs = {
				'password': {'write_only': True},
			}
			#exclude = ('password',)
			owner = serializers.ReadOnlyField(source='owner.id')

		def	save(self):

			account = Account(
						email=self.validated_data['email'],
						username=self.validated_data['username'],
						first_name=self.validated_data['first_name'],
						last_name=self.validated_data['last_name'],


					)
			password = self.validated_data['password']
			account.set_password(password)
			account.save()
			return account



# class RegistrationSerializer(serializers.ModelSerializer):

# 	password_confirmation				= serializers.CharField(style={'input_type': 'password'}, write_only=True)

# 	class Meta:
# 		model = Account
# 		fields = ['email', 'username', 'password']
# 		extra_kwargs = {
# 				'password': {'write_only': True},
# 		}


# 	def	save(self):

# 		account = Account(
# 					email=self.validated_data['email'],
# 					username=self.validated_data['username']
# 				)
# 		password = self.validated_data['password']
# 		password_confirmation = self.validated_data['password_confirmation']
# 		if password != password_confirmation:
# 			raise serializers.ValidationError({'password': 'Passwords must match.'})
# 		account.set_password(password)
# 		account.save()
# 		return account
