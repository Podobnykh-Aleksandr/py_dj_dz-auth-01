from django.contrib.auth.models import User
from rest_framework import serializers

# from api_with_restrictions.advertisements.models import Advertisement, AdvertisementStatusChoices
from advertisements.models import Advertisement, AdvertisementStatusChoices
from advertisements.filters import AdvertisementFilter


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        print(validated_data)
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        # TODO: добавьте требуемую валидацию
        advs = Advertisement.objects.filter(creator=self.context["request"].user).filter(status='OPEN').count()
        if advs >= 10 and (self.context["request"].method == 'POST' or data.get('status') == 'OPEN'):
            raise serializers.ValidationError('Достигнуто максимальное число открытых объявлений: 10')

        return data
